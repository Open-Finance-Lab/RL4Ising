import networkx as nx
import numpy as np
import os
import time
import coptpy as cp
from coptpy import COPT
from utils import read_nxgraph
from utils import float_to_binary
from utils import base64_encode

def save_to_file(model, file_path, time_limit, duration, print_terminal=True):
    
    file_dir = f"results/copt/{"/".join(file_path.split("/")[:-1])}"
    file_name = file_path.split("/")[-1]

    obj_val = model.objval
    obj_bnd = model.bestobj
    mip_gap = abs(obj_bnd - obj_val) / abs(obj_bnd)
    best_solution = "".join([ float_to_binary(x.x) for x in model.getVars() if x.name[0] == "x" ])
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


def copt_solve(graph, file_path, time_limit=3600):

    nodes = len(list(graph.nodes))
    J = nx.to_numpy_array(graph)

    env = cp.Envr()
    model = env.createModel("qubo")

    x = [ model.addVar(vtype=COPT.BINARY, name=f"x_{i}") for i in range(nodes) ]
    y = np.zeros((nodes, nodes), dtype=object)
    for i in range(nodes):
        for j in range(i +1, nodes):
            y[i, j] = model.addVar(vtype=COPT.BINARY, name=f"y_{i},{j}")
            model.addConstr(y[i, j] <= x[i])
            model.addConstr(y[i, j] <= x[j])
            model.addConstr(y[i, j] >= x[i] + x[j] - 1)

    model.setObjective(cp.quicksum(
        -J[i, j] * ( (4 * y[i,j]) + (-2 * x[i]) + (-2 * x[j]) + 1 )
        for i in range(nodes) for j in range(i + 1, nodes) if J[i, j] != 0.0 
    ), sense=COPT.MINIMIZE)
    model.setParam(COPT.Param.TimeLimit, 3600.0)
    model.setParam(COPT.Param.RelGap, 0.0)
    file_dir = f"results/copt/{"/".join(file_path.split("/")[:-1])}"
    file_name = file_path.split("/")[-1]
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    model.setLogFile(f"{file_dir}/{file_name.split(".")[0]}.log")

    start_time = time.time()
    model.solve()
    end_time = time.time()
    duration = (end_time - start_time)
    save_to_file(model, file_path, duration, time_limit)

def single_shot_instance(file_name, time_limit):
    graph = read_nxgraph(file_name)
    file_path = file_name[5:]
    copt_solve(graph, file_path, time_limit)

def multiple_shot_instance(file_names, time_limit):
    for file_name in file_names:
        single_shot_instance(file_name, time_limit)

if __name__ == "__main__":
    file_name = "../../data/DRL/2D/10/DRL_10_ID0.txt"
    time_limit = 3600
    single_shot_instance(file_name, time_limit)

    # file_names = [ "data/vna/ER/40x40_uniform_seed1.txt", "data/vna/ER/40x40_uniform_seed15.txt", "data/vna/ER/40x40_uniform_seed25.txt" ]
    # time_limit = 3600
    # multiple_shot_instance(file_names, time_limit)