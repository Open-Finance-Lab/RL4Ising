
# Baseline MIP Solvers

| Solver    | Tutorial  | Shared runner |
| --------- | :------:  | :-----------: |
| Gurobi    | [Notebook](gurobi_qubo.ipynb) | ✅ |
| IBM CPLEX | [Notebook](cplex_qubo.ipynb) | ❌ |
| COPT      | [Notebook](copt_qubo.ipynb) | ❌ |
| SCIP      | [Notebook](scip_qubo.ipynb)   | ✅ |
## Shared baseline environment

All four solvers and the baseline notebooks use `environment.yml`. From the
repository root:

```shell
conda env create -f src/baseline/environment.yml
conda activate rl4ising-baseline
python -m ipykernel install --user --name rl4ising-baseline --display-name "RL4Ising Baseline"
```

## Running SCIP and Gurobi

Run from the repository root with the baseline environment activated.
CPLEX and COPT use separate scripts.

### Single file or multiple files

```shell
python -m src.baseline.run --solver scip path/to/graph1.txt -t 3600
python -m src.baseline.run --solver gurobi path/to/graph1.txt path/to/graph2.txt -t 3600
```

### Directory batch mode

Recursively process all `.txt` graph files, preserving their directory structure:

```shell
python -m src.baseline.run --solver scip -o results src/data/graphs
python -m src.baseline.run --solver gurobi -o results src/data/graphs
```

### Command line arguments

| Flag | Long Name | Default | Description |
| :--- | :--- | :--- | :--- |
| paths | N/A | Bundled EA 10x10 test graph | Unflagged arguments specify files or directories. Directories are searched recursively for .txt graph files. |
| -s | --solver | Required | Solver to use: scip or gurobi. |
| -t | --time-limit | 3600 | Time limit for the selected solver per graph, in seconds. |
| -o | --out-dir | results | Output root. Logs, individual .txt summaries, and baseline_results.csv are saved under <out-dir>/<solver>/. Creates folders if it does not exist. |
| N/A | --retry-license | False | Retry entries that previously failed due to license_error. |
| N/A | --retry-timeouts | False | Retry entries that previously hit the time_limit. |
| -v | --verbose | False | Show solver logs in the terminal. |
| -q | --quiet | False | Hide per-graph progress output while keeping errors and final counts. |

### Outputs and progress

Each solver writes to its own folder: `results/scip/` or `results/gurobi/`.
Outputs include `baseline_results.csv`, `.txt` summaries, and `.log` files,
preserving input subfolders. Pass the output root with `-o` and the solver folder is added automatically.

The terminal shows progress, status, objective, duration, and final counts.
Solver logs are hidden by default; use `--verbose` to show them. Use `--quiet` to
hide per-graph progress while keeping errors and final counts.

### Resuming and failures

Reruns skip completed instances using the latest CSV status. Use `--retry-timeouts`
or `--retry-license` to retry timeouts or license errors. Other errors and interrupted
instances are retried automatically. Keep inputs unchanged when reusing results.

Each attempt is saved to the CSV before continuing. If a graph times out, its best solution is saved, if one was found.
If a graph fails, the batch continues to the next one. Ctrl+C stops the batch safely.
CSV write failures stop processing.
