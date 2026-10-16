import os
import sys
from pyscipopt import Model, quicksum

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import read_nxgraph, base64_encode

RESULTS_DIR = "results/scip"

def save_to_file(result, file_path, time_limit, print_terminal=True):
    target = os.path.join(RESULTS_DIR, file_path)
    os.makedirs(os.path.dirname(target), exist_ok=True)

    best_solution = result["bits"]
    best_encoded = base64_encode(best_solution) if best_solution else None
    fields = {
        "Status": result["status"],
        "Objective Value": result["objective"],
        "Objective Bound": result["bound"],
        "Duration": result["duration"],
        "Time Limit": time_limit,
        "MIP Gap": result["gap"],
        "Best Solution Encoded": best_encoded,
        "Best Solution Raw": best_solution,
    }
    text = "".join(
        f"{name}: {value if value is not None else 'N/A'}\n"
        for name, value in fields.items()
    )
    with open(target, "w") as f:
        f.write(text)

    if print_terminal:
        print(text)


def scip_solve(graph, file_path, time_limit=3600):

    # print(f"Instance: {file_path}")
    # print(f"Nodes: {graph.number_of_nodes()}")
    # print(f"Edges: {graph.number_of_edges()}")

    model = Model("ising_qubo")
    x = {node: model.addVar(vtype="B", name=f"x_{i}")
         for i, node in enumerate(graph.nodes)}

    # y = x[node1] * x[node2]
    energy_terms = []
    for i, (node1, node2, data) in enumerate(graph.edges(data=True)):
        weight = float(data["weight"])
        y = model.addVar(vtype="B", name=f"y_{i}")
        model.addConsAnd([x[node1], x[node2]], y)
        energy_terms.append(
            -weight * (4 * y - 2 * x[node1] - 2 * x[node2] + 1)
        )

    model.setObjective(quicksum(energy_terms), "minimize")
    model.setParam("limits/time", float(time_limit))
    model.setParam("limits/gap", 0.0)

    output_file = os.path.join(RESULTS_DIR, file_path)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    model.setLogfile(os.path.splitext(output_file)[0] + ".log")
    model.optimize()

    result = {
        "status": str(model.getStatus()),
        "objective": None,
        "bound": model.getDualbound(),
        "duration": model.getSolvingTime(),
        "gap": None,
        "bits": None,
    }
    if model.isInfinity(abs(result["bound"])):
        result["bound"] = None

    solution = model.getBestSol()
    if solution is not None:
        result["objective"] = model.getObjVal()
        result["gap"] = model.getGap()
        result["bits"] = "".join(
            str(round(model.getSolVal(solution, x[node]))) for node in graph.nodes
        )
        if model.isInfinity(result["gap"]):
            result["gap"] = None

    save_to_file(result, file_path, time_limit)
    model.freeProb()


def single_shot_instance(file_name, time_limit):
    graph = read_nxgraph(file_name)
    file_path = os.path.basename(file_name)
    scip_solve(graph, file_path, time_limit)


def multiple_shot_instance(file_names, time_limit):
    for file_name in file_names:
        single_shot_instance(file_name, time_limit)


if __name__ == "__main__":
    file_name = "src/tutorials/VCA/dataset/EA/EA_10x10/10x10_uniform_seed1.txt"
    time_limit = 3600
    single_shot_instance(file_name, time_limit)

