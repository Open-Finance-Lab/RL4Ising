
# Baseline MIP Solvers

| Solvers   |
|-----------|
| Gurobi    |
| ILOG CPLEX|
| COPT      |

## Gurobi Tutorial

A basic tutorial for processing files can be found gurobi_qubo.ipynb 

## gurobi.py

### Single file

python script.py path/to/graph1.txt -t 3600

### Multiple specific files

python script.py path/to/graph1.txt path/to/graph2.txt -t 3600

### Directory Batch Mode (Recommended)

Automatically finds and processes all .txt files recursively within a given directory, outputting the results to a CSV.

python script.py -i src/data/graphs -o results/gurobi/newest --csv_out batch_results.csv

---

### Command Line Arguments

| Flag | Long Name | Default | Description |
| :--- | :--- | :--- | :--- |
| paths | N/A | [specific test file] | Unflagged arguments at the end of the command are treated as manual file paths. |
| -t | --time_limit | 3600 | Time limit for the Gurobi solver per graph, in seconds. |
| -i | --in_dir | None | Input directory. Processes all .txt files found inside. |
| -o | --out_dir | results/gurobi/newest | Output directory. All .log files, individual .txt solution files, and the CSV are saved here. Creates the folder if it does not exist. |
| N/A | --csv_out | gurobi_batch_results.csv | The name of the aggregate CSV file. It is saved directly inside the --out_dir. |
| N/A | --retry_license | False | Retry entries that previously failed due to license limits. |
| N/A | --retry_timeouts | False | Retry entries that previously hit the time limit. |

### Output Structure

For every successfully solved graph, the script generates three pieces of data in the --out_dir:

1. [graph_name].log: The raw solver output straight from Gurobi, containing simplex iterations, heuristic steps, and final bounds.
2. [graph_name].txt: A summarized output file containing the Objective Value, Objective Bound, Duration, MIP Gap, and the raw binary sequence of the best solution.
3. CSV Entry: A single row in the aggregate .csv file containing the Absolute Path to the original graph and its Objective Value (or state flag like TIMEOUT / LICENSE_LIMIT).

---

### State Management

When running in Directory Batch Mode (-i), the script executes a Synchronization Phase before solving any graphs. It cross-references the existing output CSV with the .log files in the output directory to map the state of the data.

### Smart Resumption & Interruption Handling

If a batch is canceled midway using Ctrl+C, or if the system crashes:

* Clean Exits: Pressing Ctrl+C immediately halts the batch. The script will not attempt to write incomplete data to the CSV.
* Orphan Cleanup: On the next run, the script detects .log files containing "Solve interrupted". It automatically deletes these junk logs and incomplete .txt files, forcing a clean rerun of that specific graph.
* Resume Capability: Fully completed graphs recorded in the CSV (or validated by a successful .log file) are permanently skipped, allowing large batches to resume exactly where they left off.

### Timeout Management

If Gurobi reaches a defined time limit (e.g., 3600 seconds) before finding the optimal solution:

* Gurobi gracefully stops and saves the best objective value found up to that point.
* The script records this partial solution to the .txt and .log files.
* In the CSV, the value is appended with a (TIMEOUT) flag (e.g., -70.5 (TIMEOUT)) to allow for easy filtering of sub-optimal runs during data analysis.

### Directory Timeout Skipping

When processing large nested datasets, graphs within the same subfolder often share similar complexity and execution times. To optimize batch processing, the script tracks timeouts at the directory level:

* Subfolder Monitoring: If any single graph triggers a time limit (TIMEOUT) during execution, the script flags the parent subfolder.
* Automatic Bypassing: Once a subfolder is flagged, the script instantly bypasses all remaining unprocessed .txt files within that specific subfolder and moves forward to the next directory.
* Prevention of Bottlenecks: This mechanism prevents the solver from stalling on a directory filled with massive graphs, allowing the batch to continue clearing out simpler subfolders elsewhere in the dataset.

### License Limit Protection

If a graph is too large for the current Gurobi license, the solver will throw a size-limit exception.

* Instead of crashing the entire batch or entering an infinite retry loop, the script catches this specific error.
* It writes LICENSE_LIMIT to the CSV for that specific graph.
* On future runs, the script recognizes LICENSE_LIMIT as a "completed" state and skips the graph permanently, saving processing time.

### Duplicate Conflict Handling

If the script detects that a file has been processed twice with conflicting results (e.g., folders were moved and the script was run twice), it triggers an interactive terminal prompt:

[!] DUPLICATE CONFLICT: 100_SK_seed33.txt
    1: Keep First Value  -> -70.5
    2: Keep Second Value -> -71.2
    3: Delete Both (forces rerun)

If the duplicate values are identical, the script silently resolves the conflict and keeps one entry, requiring no manual input.
