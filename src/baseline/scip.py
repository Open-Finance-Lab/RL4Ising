import os

from utils import read_nxgraph, base64_encode


def save_to_file(result, file_path, time_limit, print_terminal=True):
    target = os.path.join("results/scip", file_path)
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
    print(f"Instance: {file_path}")
    print(f"Nodes: {graph.number_of_nodes()}")
    print(f"Edges: {graph.number_of_edges()}")


    result = {
        "status": "not implemented",
        "objective": None,
        "bound": None,
        "duration": None,
        "gap": None,
        "bits": None,
    }

    save_to_file(result, file_path, time_limit)


def single_shot_instance(file_name, time_limit):
    graph = read_nxgraph(file_name)
    file_path = os.path.basename(file_name)
    scip_solve(graph, file_path, time_limit)


def multiple_shot_instance(file_names, time_limit):
    for file_name in file_names:
        single_shot_instance(file_name, time_limit)


if __name__ == "__main__":
    file_name = "../../data/DRL/2D/10/DRL_10_ID0.txt"
    time_limit = 3600
    single_shot_instance(file_name, time_limit)

