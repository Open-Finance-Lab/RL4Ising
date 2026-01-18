# RL4Ising (Reinforcement Learning for Ising Models): Datasets and Benchmark

Reinforcement Learning for Ising Models is an open-source dataset and benchmark suite for Ising models. Our goal is to curate a public dataset of Ising models, provide a comprehensive benchmark of state-of-the-art reinforcement learning algorithms alongside an industry-standard solver baseline, and offer detailed tutorials for each reinforcement learning algorithm.

Explore our comprehensive benchmark suite and in-depth tutorials at [rl4ising-docs.readthedocs.io](https://rl4ising-docs.readthedocs.io/en/latest/). `<br>`
Our curated datasets of various Ising models is at [huggingface.co/datasets/SecureFinAI-Lab/Ising_Model_Instances](https://huggingface.co/datasets/SecureFinAI-Lab/Ising_Model_Instances).

## Ising Model Datasets

We curate a diverse collection of over 170,000 Ising models and construct comprehensive dataset based on dimensionality. Specifically, our dataset contains 1D, 2D, 3D, and 4D instances representing systems with finite spin interactions or nearest neighbor interactions. While the $\infty$ rank dimesion represent systems where spin interacts with every other spin regardless of spatial boundaries. Within each dimension we indentify five main types of Ising models: Classic, Spin-Glass, Ferromagnetic, Anti=Ferromagnetic, and Synthetic.

| Dimension  | Type of Ising Model | Instances |   Spins   |   Couplings   |    Coupling Strength    |
| ---------- | ------------------- | :-------: | :--------: | :------------: | :----------------------: |
| 1D         | Classic             |    75     |  32 $\textbf{--}$ 128  |    31 $\textbf{--}$ 127    |       0.00 $\textbf{--}$ 1.00       |
|            | Spin-Glass          |   4,000   |   3 $\textbf{--}$ 10   |     6 $\textbf{--}$ 55     |      -5.00 $\textbf{--}$ -4.22      |
| 2D         | Classic             |    100    |  16 $\textbf{--}$ 64  |    28 $\textbf{--}$ 120    |       -1.00 $\textbf{--}$ 1.00       |
|            | Spin-Glass          |   2,075   | 16 $\textbf{--}$ 1,600 |   32 $\textbf{--}$ 3,210   |       -5.09 $\textbf{--}$ 4.66       |
|            | Ferromagnetic       |  90,000   |   1,600   |   83 $\textbf{--}$ 1,246   |          -1.00          |
|            | Anti-Ferromagnetic  |  90,000   |   1,600   | 1,874 $\textbf{--}$ 3,037 |           1.00           |
|            | Synthetic           |     9     | 100 $\textbf{--}$ 400 |   200 $\textbf{--}$ 800   | -294,541.00 $\textbf{--}$ 375,001.00 |
| 3D         | Spin-Glass          |    666    | 24 $\textbf{--}$ 8,000 |  38 $\textbf{--}$ 40,279  |       -5.24 $\textbf{--}$ 5.03      |
|            | Synthetic           |     9     | 125 $\textbf{--}$ 343 |  375 $\textbf{--}$ 1,029  | -298,103.00 $\textbf{--}$ 375,001.00 |
|            | Diamond             |    60     |  18 $\textbf{--}$ 50  |    24 $\textbf{--}$ 80    |       -1.00 $\textbf{--}$ 1.00       |
| 4D         | Spin-Glass          |   1,450   | 81 $\textbf{--}$ 4,096 |  324 $\textbf{--}$ 16,384  |       -5.28 $\textbf{--}$ 4.97       |
| $\infty$   | Biclique            |    100    |  20 $\textbf{--}$ 36  |    35 $\textbf{--}$ 99    |       -2.00 $\textbf{--}$ 0.89       |
|            | Spin-Glass          |   5,440   |  3 $\textbf{--}$ 900  |  6 $\textbf{--}$ 319,600  |       -4.45 $\textbf{--}$ 3.92       |
|            | Synthetic           |    30     | 100 $\textbf{--}$ 300 | 4,950 $\textbf{--}$ 44,850 | -246,443.00 $\textbf{--}$ 280,065.00 |

## Benchmark Suite

Our benchmark suite consists of two integral components, a solver baseline and SOTA RL benchmark, allowing for the direct comparison of the classical optimization methods vs modern RL-based approaches.

- **Solver Baseline**: Offers transparent and provable optimal or near-optimial solutions while leveraging highly optimized, memory-efficient algorithms. Most importantly, solvers provide an upper bound enabling the measurement of solution quality for approximate methods such as RL-based algorithms.
- **SOTA RL Benchmark**: Showcases key milestones of state-of-the-art RL algorithms over the years in terms of performance and scalability. Most importantly, we highlight the current top-of-the-line RL algorithms providing high quality solutions with a scaliability and time advantage against industry solvers.

| Algorithm/Solver | Description | Reference                                                                     |
| ---------------- | ----------- | ----------------------------------------------------------------------------- |
| Gurobi           | ----------- | [1](https://www.gurobi.com)                                                      |
| IBM CPLEX        | ----------- | [2](https://www.ibm.com/docs/en/icos/22.1.1?topic=optimizers-users-manual-cplex) |
| COPT             | ----------- | [3](https://arxiv.org/abs/2208.14314)                                            |

<!-- | SCIP             | ----------- | [4](https://optimization-online.org/2024/02/the-scip-optimization-suite-9-0/)    |
| ECOLE            | ----------- | [5](https://arxiv.org/abs/2011.06069)                                            |
| MOSEK            | ----------- | [6](https://docs.mosek.com/latest/pythonfusion/index.html)                       |
| L2A              | ----------- | [7]()                                                                            |
| VCA              | ----------- | [8](https://www.nature.com/articles/s42256-021-00401-3)                          |
| MCPG             | ----------- | [9](https://arxiv.org/abs/2307.00783)                                            |
| ECO-DQN          | ----------- | [10](https://arxiv.org/abs/1909.04063)                                           |
| S2V-DQN          | ----------- | [11](https://dl.acm.org/doi/10.5555/3295222.3295382)                             | -->

### Solver Baseline

| Solvers   | Spin Glass | Ferromagnetic | Anti-Ferromagnetic | 1D Ising | 2D Ising | 3D Ising | 4D Ising |
| --------- | :--------: | :-----------: | :----------------: | :------: | :------: | :------: | :------: |
| Gurobi    |     ✅     |      ❌      |         ❌         |    ✅    |    ✅    |    ❌    |    ❌    |
| IBM CPLEX |     ✅     |      ❌      |         ❌         |    ❌    |    ❌    |    ❌    |    ❌    |
| COPT      |     ✅     |      ❌      |         ❌         |    ✅    |    ✅    |    ❌    |    ❌    |
| SCIP      |     ❌     |      ❌      |         ❌         |    ❌    |    ❌    |    ❌    |    ❌    |
| ECOLE     |     ❌     |      ❌      |         ❌         |    ❌    |    ❌    |    ❌    |    ❌    |
| MOSEK     |     ❌     |      ❌      |         ❌         |    ❌    |    ❌    |    ❌    |    ❌    |

### Benchmarks

| Becnhmark | Spin Glass | Ferromagnetic | Anti-Ferromagnetic | 1D Ising | 2D Ising | 3D Ising | 4D Ising |
| --------- | :--------: | :-----------: | :----------------: | :------: | :------: | :------: | :------: |
| L2A       |     ✅     |      ❌      |         ❌         |    ✅    |    ✅    |    ❌    |    ❌    |
| VCA       |     ✅     |      ❌      |         ❌         |    ❌    |    ❌    |    ❌    |    ❌    |
| MCPG      |     ✅     |      ❌      |         ❌         |    ✅    |    ✅    |    ❌    |    ❌    |
| ECO-DQN   |     ❌     |      ❌      |         ❌         |    ❌    |    ❌    |    ❌    |    ❌    |
| S2V-DQN   |     ❌     |      ❌      |         ❌         |    ❌    |    ❌    |    ❌    |    ❌    |

## Tutorials

## File Structure

```
    ├── docs            : ReadTheDocs website containing algorithms, tutorials, and dataset overview. 
    |
    └── src
        ├── algorithms
        |   ├── vca                 : Variational Classical Annealing algorithm.
        |   ├── mcpg                : Monte Carlo Policy Gradient algorithm modified for Ising models.
        |   ├── eco_dqn             : Exploratory Combinatorial Optimization with Reinforcement Learning modified for Ising models.
        |   └── vta                 : Variational Transformer Annealing algorithm, transformer based VCA.
        |   
        ├── baseline
        |   ├── gurobi.py           : Gurobi MIP Solver.
        |   ├── ilog_cplex.py       : IBM ILOG CPLEX MIP Solver.
        |   └── copt.py             : COPT Cardinal MIP Solver.
        |
        └── tutorials
            ├── vca.ipynb           : VCA tutorial for EA 100 node instance.
            ├── mcpg.ipynb          : MCPG tutorial for EA 100 node instance.
            └── eco_dqn.ipynb       : ECO-DQN tutorial for EA 100 node instance.



```

## Reference
Lin, L., Wang, Z., Mac Entee, H., Zhao, X., & Liu, X.-Y.  
*Reinforcement Learning for Ising Models: Datasets and Benchmark*,  
NeurIPS ML4PS Workshop, 2025.  
[PDF](https://ml4physicalsciences.github.io/2025/files/NeurIPS_ML4PS_2025_245.pdf)


