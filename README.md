# RL4Ising (Reinforcement Learning for Ising Models): Datasets and Benchmark
Reinforcement Learning for Ising Models is an open-source dataset and benchmark suite for Ising models. Our goal is to curate a public dataset of Ising models, provide a comprehensive benchmark of state-of-the-art reinforcement learning algorithms alongside an industry-standard solver baseline, and offer detailed tutorials for each reinforcement learning algorithm. 

Explore our comprehensive benchmark suite and in-depth tutorials at [rl4ising-docs.readthedocs.io](https://rl4ising-docs.readthedocs.io/en/latest/). <br>
Our curated datasets of various Ising models is at [huggingface.co/datasets/SecureFinAI-Lab/Ising_Model_Instances](https://huggingface.co/datasets/SecureFinAI-Lab/Ising_Model_Instances).

## Ising Model Datasets
We curate a diverse collection of over 170,000 Ising models and construct two distinct datasets:

- **Dataset 1**: Classification based on spin interactions
- **Dataset 2**: Classification based on model dimensionality

### Dataset 1

| Types of Ising Models | Description | Instances | Spin Range | Coupling Range |
| --------------------- | ----------- | :-------: | :--------: | :------------: |
| Spin Glass            | ...         | 14,045    | 0 - 0      | 0 - 0          | 
| Ferromagnetic         | ...         | 90,000    | 0 - 0      | 0 - 0          | 
| Anti-Ferromagnetic    | ...         | 90,007    | 0 - 0      | 0 - 0          | 

### Dataset 2

| Types of Ising Models | Description | Instances | Spin Range | Coupling Range |
| --------------------- | ----------- | :-------: | :--------: | :------------: |
| 1D ising Models       | ...         |           | 0 - 0      | 0 - 0          |
| 2D ising Models       | ...         |           | 0 - 0      | 0 - 0          | 
| 3D ising Models       | ...         |           | 0 - 0      | 0 - 0          | 
| 4D ising Models       | ...         |           | 0 - 0      | 0 - 0          | 

## Benchmark Suite
Our benchmark suite consists of two integral components, a solver baseline and SOTA RL benchmark, allowing for the direct comparison of the classical optimization methods vs modern RL-based approaches.

- **Solver Baseline**: Offers transparent and provable optimal or near-optimial solutions while leveraging highly optimized, memory-efficient algorithms. Most importantly, solvers provide an upper bound enabling the measurement of solution quality for approximate methods such as RL-based algorithms. 
- **SOTA RL Benchmark**: Showcases key milestones of state-of-the-art RL algorithms over the years in terms of performance and scalability. Most importantly, we highlight the current top-of-the-line RL algorithms providing high quality solutions with a scaliability and time advantage against industry solvers.

| Algorithm/Solver | Description | Reference                          |
| ---------------- | ----------- | ---------------------------------- |
| Gurobi           | ----------- | [1](https://www.gurobi.com)        |
| IBM CPLEX        | ----------- | [2](https://www.ibm.com/docs/en/icos/22.1.1?topic=optimizers-users-manual-cplex) |
| COPT             | ----------- | [3](https://arxiv.org/abs/2208.14314) |
| SCIP             | ----------- | [4](https://optimization-online.org/2024/02/the-scip-optimization-suite-9-0/) |
| ECOLE            | ----------- | [5](https://arxiv.org/abs/2011.06069) |
| MOSEK            | ----------- | [6](https://docs.mosek.com/latest/pythonfusion/index.html) |
| L2A              | ----------- | [7]() |
| VCA              | ----------- | [8](https://www.nature.com/articles/s42256-021-00401-3) |
| MCPG             | ----------- | [9](https://arxiv.org/abs/2307.00783) |
| ECO-DQN          | ----------- | [10](https://arxiv.org/abs/1909.04063) |
| S2V-DQN          | ----------- | [11](https://dl.acm.org/doi/10.5555/3295222.3295382) |


### Solver Baseline

| Solvers   | Spin Glass         | Ferromagnetic      | Anti-Ferromagnetic | 1D Ising           | 2D Ising           | 3D Ising           | 4D Ising           |
| --------- | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: |
| Gurobi    | :white_check_mark: | :x:                | :x:                | :white_check_mark: | :white_check_mark: | :x:                | :x:                |
| IBM CPLEX | :white_check_mark: | :x:                | :x:                | :x:                | :x:                | :x:                | :x:                |
| COPT      | :white_check_mark: | :x:                | :x:                | :white_check_mark: | :white_check_mark: | :x:                | :x:                |
| SCIP      | :x:                | :x:                | :x:                | :x:                | :x:                | :x:                | :x:                |
| ECOLE     | :x:                | :x:                | :x:                | :x:                | :x:                | :x:                | :x:                |
| MOSEK     | :x:                | :x:                | :x:                | :x:                | :x:                | :x:                | :x:                |

### Benchmarks

| Becnhmark | Spin Glass         | Ferromagnetic      | Anti-Ferromagnetic | 1D Ising           | 2D Ising           | 3D Ising           | 4D Ising           |
| --------- | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: |
| L2A       | :white_check_mark: | :x:                | :x:                | :white_check_mark: | :white_check_mark: | :x:                | :x:                |
| VCA       | :white_check_mark: | :x:                | :x:                | :x:                | :x:                | :x:                | :x:                |
| MCPG      | :white_check_mark: | :x:                | :x:                | :white_check_mark: | :white_check_mark: | :x:                | :x:                |
| ECO-DQN   | :x:                | :x:                | :x:                | :x:                | :x:                | :x:                | :x:                |
| S2V-DQN   | :x:                | :x:                | :x:                | :x:                | :x:                | :x:                | :x:                |


## Tutorials

## File Structure
```
    ├── docs           : RL4Ising website. 
    └── tutorials      : MIP solver and RL algorithm tutorials.
```

## Motivation
