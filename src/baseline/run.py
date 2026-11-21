import argparse
import csv
from importlib import import_module
from pathlib import Path

from .utils import base64_encode, read_nxgraph


def write_result(result, output_path):
    bits = result["bits"]
    fields = {
        "Status": result["status"],
        "Objective Value": result["objective"],
        "Objective Bound": result["bound"],
        "Duration": result["duration"],
        "Time Limit": result["time_limit"],
        "MIP Gap": result["gap"],
        "Best Solution Encoded": base64_encode(bits) if bits else None,
        "Best Solution Raw": bits,
    }
    text = "".join(
        f"{name}: {value if value is not None else 'N/A'}\n"
        for name, value in fields.items()
    )
    Path(output_path).write_text(text)


def run_single_file(input_path, time_limit=3600, out_dir="results", solver="scip", verbose=False):
    adapter = import_module(f".{solver}", package=__spec__.parent)
    
    input_path = Path(input_path)
    output_path = Path(out_dir) / f"{input_path.stem}.txt"
    log_path = output_path.with_suffix(".log")

    if input_path.resolve() in (output_path.resolve(), log_path.resolve()):
        raise ValueError(f"Output would overwrite input: {input_path}")
    
    graph = read_nxgraph(str(input_path))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result = adapter.solve(graph, time_limit, log_path, verbose)
    write_result(result, output_path)
    return result

def prepare_runs(paths, out_dir, output_root=None):
    out_dir = Path(out_dir).resolve()
    output_root = Path(output_root).resolve() if output_root is not None else out_dir
    jobs = []
    inputs = set()
    outputs = {(out_dir / "baseline_results.csv").resolve()}
    seen = set()

    for path in paths:
        source = Path(path).resolve()
        is_directory = source.is_dir()
        output_is_subdirectory = (
            is_directory
            and output_root != source
            and output_root.is_relative_to(source)
        )
        files = sorted(source.rglob("*.txt")) if is_directory else [source]

        for file in files:
            if is_directory and not file.is_file():
                continue

            resolved_file = file.resolve()

            # Skip saved results in the output folder.
            if output_is_subdirectory and resolved_file.is_relative_to(output_root):
                continue
            
            # Keep the same input folder structure in the results.
            relative = file.relative_to(source) if is_directory else Path(file.name)
            target = (out_dir / relative).with_suffix(".txt")
            input_output_pair = (resolved_file, target.resolve())

            if input_output_pair in seen:
                continue
            seen.add(input_output_pair)
            inputs.add(resolved_file)

            # Prevent different graphs from writing to the same result files.
            for output in (target, target.with_suffix(".log")):
                output = output.resolve()
                if output in outputs:
                    raise ValueError(f"Output collision: {output}")
                outputs.add(output)

            jobs.append((file, target.parent))

    # Check every output path before any solver starts.
    for output in outputs:
        if output in inputs:
            raise ValueError(f"Output would overwrite input: {output}")

        if any(parent in outputs for parent in output.parents):
            raise ValueError(f"Output file conflicts with an output directory: {output}")

        if output.is_dir() or any(parent.is_file() for parent in output.parents):
            raise ValueError(f"Output path is blocked: {output}")

    return jobs


def load_previous_results(csv_path, fields):
    latest_statuses = {}
    needs_newline = False

    has_header = csv_path.exists() and csv_path.stat().st_size > 0

    # Load previous csv results so completed graphs can be skipped on reruns.
    if has_header:
        with csv_path.open(newline="", encoding="utf-8") as stream:
            reader = csv.DictReader(stream)

            if reader.fieldnames != list(fields):
                raise ValueError(f"Unexpected CSV columns: {csv_path}")

            for row in reader:
                if None in row or any(value is None for value in row.values()):
                    raise ValueError(f"Incomplete CSV record: {csv_path}")

                input_path = str(Path(row["input_path"]).resolve())
                
                # Keep the latest status for each graph and solver.
                key = (input_path, row["solver"])
                latest_statuses[key] = row["status"]
                
        # Check if the CSV needs a newline before adding more results.
        with csv_path.open("rb") as stream:
            stream.seek(-1, 2)
            needs_newline = stream.read(1) not in (b"\n", b"\r")

    return latest_statuses, has_header, needs_newline


def run_batch(jobs, solver, time_limit, out_dir, retry_timeouts=False, retry_license=False, verbose=False, quiet=False):
    output_dir = Path(out_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    fields = ("input_path", "solver", "status", "objective", "bound", "duration", "time_limit", "gap")
    csv_path = output_dir / "baseline_results.csv"
    latest_statuses, has_header, needs_newline = load_previous_results(csv_path, fields)

    statuses_to_skip = {"optimal", "infeasible", "unbounded", "infeasible_or_unbounded", "limit"}
    
    if not retry_timeouts:
        statuses_to_skip.add("time_limit")
    if not retry_license:
        statuses_to_skip.add("license_error")
        
    processed = skipped = failures = 0
    with csv_path.open("a", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        if not has_header:
            writer.writeheader()
        elif needs_newline:
            stream.write("\n")
        stream.flush()
            
            
        for index, (file, graph_out_dir) in enumerate(jobs, 1):
            progress = f"[{index}/{len(jobs)}]"
            display_path = (graph_out_dir.resolve() / file.name).relative_to(output_dir).as_posix()
            
            # Skip this graph if its previous result for this solver doesn't need retrying.
            key = (str(file.resolve()), solver)
            if latest_statuses.get(key) in statuses_to_skip:
                skipped += 1
                if not quiet:
                    print(f"{progress} Skipping {display_path}: {latest_statuses[key]}", flush=True)
                continue

            if not quiet:
                print(f"{progress} Solving {display_path}...", flush=True)

            result = {"status": "error", "objective": None, "bound": None,
                      "duration": None, "time_limit": time_limit, "gap": None, "bits": None}
            try:
                result = run_single_file(file, time_limit, graph_out_dir, solver, verbose)
            except KeyboardInterrupt:
                result["status"] = "interrupted"
            except Exception as exc:
                print(f"Error solving {display_path}: {exc}")
                
            # Save each result before moving on. Stop if saving fails.
            writer.writerow({
                "input_path": str(file.resolve()),
                "solver": solver,
                "status": result["status"],
                "objective": result["objective"],
                "bound": result["bound"],
                "duration": result["duration"],
                "time_limit": result["time_limit"],
                "gap": result["gap"],
            })
            stream.flush()
            latest_statuses[key] = result["status"]
            processed += 1
            if not quiet:
                objective = f"{result['objective']:.6g}" if result["objective"] is not None else "N/A"
                duration = f"{result['duration']:.2f}s" if result["duration"] is not None else "N/A"
                print(f"{progress} {result['status']} | objective={objective} | duration={duration}", flush=True)
            if result["status"] == "interrupted":
                print(f"Interrupted: {processed} processed, {skipped} skipped, {failures} failed", flush=True)
                return 130
            if result["status"] in ("error", "license_error"):
                failures += 1

    print(f"Finished: {processed} processed, {skipped} skipped, {failures} failed", flush=True)
    return 1 if failures else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Run baseline solver on graphs.")
    
    parser.add_argument(
        "-s",
        "--solver", 
        required=True,
        choices=["scip", "gurobi"]
    )
    
    parser.add_argument(
        "-t", 
        "--time-limit", 
        type=int, 
        default=3600,
        help="Time limit for the solver in seconds (default: 3600).",
    )
    
    parser.add_argument(
        "-o", 
        "--out-dir", 
        default="results",
        help="Output root; results go in <out-dir>/<solver>/ (default: results).",
    )
    
    parser.add_argument(
        "--retry-timeouts", 
        action="store_true",
        help="Retry graphs whose latest CSV status is time_limit.")
    
    parser.add_argument(
        "--retry-license", 
        action="store_true",
        help="Retry graphs whose latest CSV status is license_error.")

    parser.add_argument(
        "-v",
        "--verbose", 
        action="store_true", 
        help="Show solver logs in the terminal.")

    parser.add_argument(
        "-q", 
        "--quiet", 
        action="store_true",
        help="Hide per-graph progress output while keeping errors and final counts.")

    parser.add_argument(
        "paths",
        nargs="*",
        default=["src/tutorials/VCA/dataset/EA/EA_10x10/10x10_uniform_seed1.txt"],
        help="One or more files or directories (recursively process .txt files). Defaults to a specific test file if omitted.",
    )
    
    args = parser.parse_args(argv)

    output_dir = Path(args.out_dir) / args.solver
    jobs = prepare_runs(args.paths, output_dir, args.out_dir)
    return run_batch(jobs, args.solver, args.time_limit, output_dir, args.retry_timeouts, args.retry_license, args.verbose, args.quiet)


if __name__ == "__main__":
    raise SystemExit(main())
