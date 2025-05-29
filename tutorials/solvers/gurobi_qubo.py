import networkx as nx
import numpy as np
import os
import gurobipy as gp
from utils import read_nxgraph
from utils import float_to_binary
from utils import base64_encode

def save_to_file(model, file_path, time_limit, print_terminal=True):
    
    file_dir = f"results/gurobi/{"/".join(file_path.split("/")[:-1])}"
    file_name = file_path.split("/")[-1]

    obj_val = model.ObjVal
    obj_bnd = model.ObjBound
    duration = model.Runtime
    mip_gap = model.MIPGap
    best_solution = "".join([ float_to_binary(x.X) for x in model.getVars() ])
    best_encoded = base64_encode(best_solution)

    with open(f"{file_dir}/{file_name}", "w") as f:
        f.write(f"Objective Value: {obj_val}\n")
        f.write(f"Objective Bound: {obj_bnd}\n")
        f.write(f"Duration: {duration}\n")
        f.write(f"Time Limit: {time_limit}\n")
        f.write(f"MIP Gap: {mip_gap}\n")
        f.write(f"Best Solution Encoded: {best_encoded}\n")
        f.write(f"Best Solution Raw: {best_solution}\n")

    if print_terminal:
        print(f"Objective Value: {obj_val}")
        print(f"Objective Bound: {obj_bnd}")
        print(f"Duration: {duration}")
        print(f"Time Limit: {time_limit}")
        print(f"MIP Gap: {mip_gap}")
        print(f"Best Solution Encoded: {best_encoded}")
        print(f"Best Solution Raw: {best_solution}\n")


def gurobi_solve(graph, file_path, time_limit=3600):

    nodes = len(list(graph.nodes))
    J = nx.to_numpy_array(graph)

    model = gp.Model("maxcut_qubo")

    x = model.addVars(nodes, vtype=gp.GRB.BINARY)
    objective = gp.quicksum(
        -J[i, j] * (2 * x[i] - 1) * (2 * x[j] - 1)
        for i in range(nodes) for j in range(i+1, nodes) if J[i, j] != 0.0
    )
    model.setObjective(objective, gp.GRB.MINIMIZE)
    model.setParam('TimeLimit', time_limit)    
    model.setParam("MIPGap", 0.0)

    file_dir = f"results/gurobi/{"/".join(file_path.split("/")[:-1])}"
    file_name = file_path.split("/")[-1]
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    model.Params.LogFile = f"{file_dir}/{file_name.split(".")[0]}.log"

    model.optimize()
    save_to_file(model, file_path, time_limit)

def single_shot_instance(file_name, time_limit):
    graph = read_nxgraph(file_name)
    file_path = file_name[5:]
    gurobi_solve(graph, file_path, time_limit)

def multiple_shot_instance(file_names, time_limit):
    for file_name in file_names:
        single_shot_instance(file_name, time_limit)

if __name__ == "__main__":
    file_name = "data/vna/ER/40x40_uniform_seed1.txt"
    time_limit = 3600
    single_shot_instance(file_name, time_limit)

    # file_names = [ "data/vna/ER/40x40_uniform_seed1.txt", "data/vna/ER/40x40_uniform_seed15.txt", "data/vna/ER/40x40_uniform_seed25.txt" ]
    # time_limit = 3600
    # multiple_shot_instance(file_names, time_limit)