import networkx as nx
import gurobipy as gp


def extract_result(model, x, time_limit):
    statuses = {
        gp.GRB.OPTIMAL: "optimal",
        gp.GRB.TIME_LIMIT: "time_limit",
        gp.GRB.INTERRUPTED: "interrupted",
        gp.GRB.INFEASIBLE: "infeasible",
        gp.GRB.UNBOUNDED: "unbounded",
        gp.GRB.INF_OR_UNBD: "infeasible_or_unbounded",
        gp.GRB.NUMERIC: "error",
    }
    
    result = {
        "status": statuses.get(model.Status, "limit"),
        "objective": None,
        "bound": None,
        "duration": model.Runtime,
        "time_limit": time_limit,
        "gap": None,
        "bits": None,
    }
    
    try:
        bound = model.ObjBound
        result["bound"] = bound if abs(bound) < gp.GRB.INFINITY else None
    except AttributeError:
        pass
    
    if model.SolCount > 0:
        result["objective"] = model.ObjVal
        gap = model.MIPGap
        result["gap"] = gap if abs(gap) < gp.GRB.INFINITY else None
        result["bits"] = "".join(
            str(round(variable.X)) for variable in x.values()
        )
    return result


def solve(graph, time_limit=3600, log_path=None, verbose=False):
    nodes = len(graph.nodes)
    J = nx.to_numpy_array(graph)
    try:
        with gp.Env(params={"LogToConsole": int(verbose)}) as env, gp.Model("maxcut_qubo", env=env) as model:
            x = model.addVars(nodes, vtype=gp.GRB.BINARY)
            objective = gp.quicksum(
                -J[i, j] * (2 * x[i] - 1) * (2 * x[j] - 1)
                for i in range(nodes)
                for j in range(i + 1, nodes)
                if J[i, j] != 0.0
            )
            model.setObjective(objective, gp.GRB.MINIMIZE)
            model.setParam("TimeLimit", time_limit)
            model.setParam("MIPGap", 0.0)
            if log_path is not None:
                model.Params.LogFile = str(log_path)
            model.optimize()

            return extract_result(model, x, time_limit)
    except gp.GurobiError as exc:
        if exc.errno not in (gp.GRB.Error.NO_LICENSE, gp.GRB.Error.SIZE_LIMIT_EXCEEDED):
            raise
        print(f"Gurobi license error: {exc}")
        return {
            "status": "license_error", "objective": None, "bound": None,
            "duration": None, "time_limit": time_limit, "gap": None, "bits": None,
        }
