from pyscipopt import Model, quicksum


def extract_result(model, x, time_limit):
    statuses = {
        "optimal": "optimal",
        "timelimit": "time_limit",
        "userinterrupt": "interrupted",
        "infeasible": "infeasible",
        "unbounded": "unbounded",
        "inforunbd": "infeasible_or_unbounded",
        "unknown": "error",
    }
    
    result = {
        "status": statuses.get(model.getStatus(), "limit"),
        "objective": None,
        "bound": model.getDualbound(),
        "duration": model.getSolvingTime(),
        "time_limit": time_limit,
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
            str(round(model.getSolVal(solution, variable))) for variable in x.values()
        )
        if model.isInfinity(result["gap"]):
            result["gap"] = None

    return result


def solve(graph, time_limit=3600, log_path=None, verbose=False):

    model = Model("ising_qubo")
    try:
        model.hideOutput(not verbose)
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

        if log_path is not None:
            model.setLogfile(str(log_path))
        model.optimize()

        return extract_result(model, x, time_limit)
    finally:
        model.freeProb()
