"""
Copyright (c) 2024 Cheng Chen, Ruitao Chen, Tianyou Li, Zaiwen Wen
All rights reserved.
Redistribution and use in source and binary forms, with or without modification, are permitted provided that
the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the
   following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions
   and the following disclaimer in the documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import torch
import os
from torch_geometric.data import Data
import numpy as np
import scipy.io as scio

def dataloader_select(problem_type):
    if problem_type == "ising":
        return maxcut_dataloader
    else:
        raise (Exception("Unrecognized problem type {}".format(problem_type)))

def maxcut_dataloader(path, device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')):
    with open(path) as f:
        fline = f.readline()
        fline = fline.split()
        num_nodes, num_edges = int(fline[0]), int(fline[1])
        edge_index = torch.LongTensor(2, num_edges)
        edge_attr = torch.Tensor(num_edges, 1)
        cnt = 0
        while True:
            lines = f.readlines(num_edges * 2)
            if not lines:
                break
            for line in lines:
                line = line.rstrip('\n').split()
                edge_index[0][cnt] = int(line[0]) - 1
                edge_index[1][cnt] = int(line[1]) - 1
                edge_attr[cnt][0] = float(line[2])
                cnt += 1
        data_maxcut = Data(num_nodes=num_nodes,
                           edge_index=edge_index, edge_attr=edge_attr)
        data_maxcut = data_maxcut.to(device)
        data_maxcut.edge_weight_sum = float(torch.sum(data_maxcut.edge_attr))

        data_maxcut = append_neighbors(data_maxcut)

        data_maxcut.single_degree = []
        data_maxcut.weighted_degree = []
        tensor_abs_weighted_degree = []
        for i0 in range(data_maxcut.num_nodes):
            data_maxcut.single_degree.append(len(data_maxcut.neighbors[i0]))
            data_maxcut.weighted_degree.append(
                float(torch.sum(data_maxcut.neighbor_edges[i0])))
            tensor_abs_weighted_degree.append(
                float(torch.sum(torch.abs(data_maxcut.neighbor_edges[i0]))))
        tensor_abs_weighted_degree = torch.tensor(tensor_abs_weighted_degree)
        data_maxcut.sorted_degree_nodes = torch.argsort(
            tensor_abs_weighted_degree, descending=True)

        edge_degree = []
        add = torch.zeros(3, num_edges).to(device)
        for i0 in range(num_edges):
            edge_degree.append(abs(edge_attr[i0].item())*(
                tensor_abs_weighted_degree[edge_index[0][i0]]+tensor_abs_weighted_degree[edge_index[1][i0]]))
            node_r = edge_index[0][i0]
            node_c = edge_index[1][i0]
            add[0][i0] = - data_maxcut.weighted_degree[node_r] / \
                2 + data_maxcut.edge_attr[i0] - 0.05
            add[1][i0] = - data_maxcut.weighted_degree[node_c] / \
                2 + data_maxcut.edge_attr[i0] - 0.05
            add[2][i0] = data_maxcut.edge_attr[i0]+0.05

        for i0 in range(num_nodes):
            data_maxcut.neighbor_edges[i0] = data_maxcut.neighbor_edges[i0].unsqueeze(
                0)
        data_maxcut.add = add
        edge_degree = torch.tensor(edge_degree)
        data_maxcut.sorted_degree_edges = torch.argsort(
            edge_degree, descending=True)

        return data_maxcut, num_nodes


def append_neighbors(data, device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')):
    data.neighbors = []
    data.neighbor_edges = []
    num_nodes = data.num_nodes
    for i in range(num_nodes):
        data.neighbors.append([])
        data.neighbor_edges.append([])
    edge_number = data.edge_index.shape[1]

    for index in range(0, edge_number):
        row = data.edge_index[0][index]
        col = data.edge_index[1][index]
        edge_weight = data.edge_attr[index][0].item()

        data.neighbors[row].append(col.item())
        data.neighbor_edges[row].append(edge_weight)
        data.neighbors[col].append(row.item())
        data.neighbor_edges[col].append(edge_weight)

    data.n0 = []
    data.n1 = []
    data.n0_edges = []
    data.n1_edges = []
    for index in range(0, edge_number):
        row = data.edge_index[0][index]
        col = data.edge_index[1][index]
        data.n0.append(data.neighbors[row].copy())
        data.n1.append(data.neighbors[col].copy())
        data.n0_edges.append(data.neighbor_edges[row].copy())
        data.n1_edges.append(data.neighbor_edges[col].copy())
        i = 0
        for i in range(len(data.n0[index])):
            if data.n0[index][i] == col:
                break
        data.n0[index].pop(i)
        data.n0_edges[index].pop(i)
        for i in range(len(data.n1[index])):
            if data.n1[index][i] == row:
                break
        data.n1[index].pop(i)
        data.n1_edges[index].pop(i)

        data.n0[index] = torch.LongTensor(data.n0[index]).to(device)
        data.n1[index] = torch.LongTensor(data.n1[index]).to(device)
        data.n0_edges[index] = torch.tensor(
            data.n0_edges[index]).unsqueeze(0).to(device)
        data.n1_edges[index] = torch.tensor(
            data.n1_edges[index]).unsqueeze(0).to(device)

    for i in range(num_nodes):
        data.neighbors[i] = torch.LongTensor(data.neighbors[i]).to(device)
        data.neighbor_edges[i] = torch.tensor(
            data.neighbor_edges[i]).to(device)

    return data