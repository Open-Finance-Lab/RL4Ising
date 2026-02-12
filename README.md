# RL4Ising (Reinforcement Learning for Ising Models): Datasets and Benchmark

Reinforcement Learning for Ising Models is an open-source dataset and reinforcement learning benchmark suite for Ising models. Our goal is to curate a comprehensive public dataset of Ising models, provide a state-of-the-art (SOTA) reinforcement learning benchmark using industry-standard mixed-integer programming (MIP) solvers as a baseline, and offer detailed tutorials for each reinforcement learning algorithm.

Our curated datasets of various Ising models is at [huggingface.co/datasets/SecureFinAI-Lab/Ising_Model_Instances](https://huggingface.co/datasets/SecureFinAI-Lab/Ising_Model_Instances).

Explore our comprehensive benchmark suite and in-depth tutorials at [rl4ising-docs.readthedocs.io](https://rl4ising-docs.readthedocs.io/en/latest/).

## Ising Model Dataset

We curate a diverse collection of over 190,000 Ising models and rank Ising model instances based on dimensionality. We categorize five dimensions: 1D, 2D, 3D, 4D, and $\infty$.

- 1D, 2D, 3D, 4D: Systems with finite spin interactions or nearest neighbor interactions.
- $\infty$: Systems where spin interacts with every other spin regardless of spatial boundaries.

Within each dimension rank we further specify Ising model instances into five main types of Ising models: Classic, Spin-Glass, Ferromagnetic, Anti-Ferromagnetic, and Synthetic.

- Classic: The basic Ising model composed of neighboring spins interactions and a typical coupling strength of $J_{ij} \in [0, +1]$ or $J_{ij} \in [-1, +1]$.
- Spin-Glass: A disordered and frustrated variant of the Classic Ising model caused by random coupling strengths, $J_{ij}$, typically gaussian distributed.
- Ferromagnetic: A variant of the Classic Ising model, where spins prefer to be aligned and coupling strengths are $J_{ij} > 0$.
- Anti-Ferromagnetic: A variant of the Classic Ising model, where spins prefer to be anti-aligned and coupling strengths are $J_{ij} < 0$.
- Synthetic: Artificial Ising models designed to model specific network or physical systems and embed artificial complexity via extremely large or small coupling strengths, $J_{ij}$.

A breakdown of the content of our datset is found as a table below.

| Dimension  | Type of Ising Model | Instances |          Spins          |          Couplings          |           Coupling Strength           |
| ---------- | ------------------- | :-------: | :---------------------: | :-------------------------: | :-----------------------------------: |
| 1D         | Classic             |    75    |  32 $\textbf{--}$ 128  |    31 $\textbf{--}$ 127    |       0.00 $\textbf{--}$ 1.00       |
|            | Spin-Glass          |   4,000   |   3 $\textbf{--}$ 10   |     6 $\textbf{--}$ 55     |      -5.00 $\textbf{--}$ -4.22      |
| 2D         | Classic             |    100    |  16 $\textbf{--}$ 64  |    28 $\textbf{--}$ 120    |       -1.00 $\textbf{--}$ 1.00       |
|            | Spin-Glass          |   2,075   | 16 $\textbf{--}$ 1,600 |   32 $\textbf{--}$ 3,210   |       -5.09 $\textbf{--}$ 4.66       |
|            | Ferromagnetic       |  90,000  |          1,600          |   83 $\textbf{--}$ 1,246   |                 -1.00                 |
|            | Anti-Ferromagnetic  |  90,000  |          1,600          | 1,874 $\textbf{--}$ 3,037 |                 1.00                 |
|            | Synthetic           |     9     | 100 $\textbf{--}$ 400 |   200 $\textbf{--}$ 800   | -294,541.00 $\textbf{--}$ 375,001.00 |
| 3D         | Spin-Glass          |    666    | 24 $\textbf{--}$ 8,000 |  38 $\textbf{--}$ 40,279  |       -5.24 $\textbf{--}$ 5.03       |
|            | Synthetic           |     9     | 125 $\textbf{--}$ 343 |  375 $\textbf{--}$ 1,029  | -298,103.00 $\textbf{--}$ 375,001.00 |
|            | Diamond             |    60    |  18 $\textbf{--}$ 50  |    24 $\textbf{--}$ 80    |       -1.00 $\textbf{--}$ 1.00       |
| 4D         | Spin-Glass          |   1,450   | 81 $\textbf{--}$ 4,096 |  324 $\textbf{--}$ 16,384  |       -5.28 $\textbf{--}$ 4.97       |
| $\infty$ | Biclique            |    100    |  20 $\textbf{--}$ 36  |    35 $\textbf{--}$ 99    |       -2.00 $\textbf{--}$ 0.89       |
|            | Spin-Glass          |   5,440   |  3 $\textbf{--}$ 900  |  6 $\textbf{--}$ 319,600  |       -4.45 $\textbf{--}$ 3.92       |
|            | Synthetic           |    30    | 100 $\textbf{--}$ 300 | 4,950 $\textbf{--}$ 44,850 | -246,443.00 $\textbf{--}$ 280,065.00 |

Clone our dataset via the following command:

```
git clone https://huggingface.co/datasets/SecureFinAI-Lab/Ising_Model_Instances
```

## Reinforcement Learning Benchmark Suite

Our reinforcement learning benchmark suite consists of a mixed-integer programming solver baseline and SOTA RL benchmark, allowing for the direct comparison of the heuristic methods against modern RL-based approaches.

- **Solver Baseline**: Offers transparent and provable optimal or near-optimal solutions while leveraging highly optimized, memory-efficient algorithms. Solvers also provide an quick high-quality approximation of the problem's lower bound enabling a simple but effective measurement of solutions between solvers vs RL algorithms and RL algorithms vs RL algorithms, via the mixed-integer programming gap metric.
- **SOTA RL Benchmark**: Showcase the performance of current state-of-the-art RL algorithms against the NP-hard problem in Ising models. Using this benchmark suite we showcase the current gap in research by highlighting the gap between our current high quality approximations and the theorical lower bound on scaling Ising models.

| Type of Method          | Name      | Description                                                    | Reference                                                                                |
| ----------------------- | --------- | -------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **MIP Solvers**   | Gurobi    | Industry leading solver.                                       | [Gurobi Manual](https://docs.gurobi.com/projects/optimizer/en/current/index.html)           |
|                         | IBM CPLEX | Top-tier commerical solver and major competitor.               | [CPLEX Manual](https://www.ibm.com/docs/en/icos/22.1.1?topic=optimizers-users-manual-cplex) |
|                         | COPT      | High-performance commerical solver for large scale instances.  | [COPT Manual](https://guide.coap.online/copt/en-doc/)                                       |
|                         | SCIP      | Fastest open-source solver alternative.                        | [SCIP Manual](https://www.scipopt.org/doc-8.0.0/html/)                                      |
| **RL Algorithms** | VCA       | Autogressive RNN-enhanced simulated annealing sampling method. | [(Mohamed Hibat-Allah et al., 2021)](https://doi.org/10.1038/s42256-021-00401-3)            |
|                         | MCPG      | A policy gradient-enhanced Monte Carlo sampling method.        | [(Cheng Chen et al., 2023)](https://arxiv.org/abs/2307.00783)                               |

| Solver    | 1D Ising | 2D Ising | 3D Ising | 4D Ising |
| --------- | :------: | :------: | :------: | :------: |
| Gurobi    |    ✅    |    ✅    |    ❌    |    ❌    |
| IBM CPLEX |    ❌    |    ❌    |    ❌    |    ❌    |
| COPT      |    ✅    |    ✅    |    ❌    |    ❌    |

| Benchmark | 1D Ising | 2D Ising | 3D Ising | 4D Ising |
| --------- | :------: | :------: | :------: | :------: |
| L2A       |    ✅    |    ✅    |    ❌    |    ❌    |
| VCA       |    ❌    |    ❌    |    ❌    |    ❌    |
| MCPG      |    ✅    |    ✅    |    ❌    |    ❌    |

## Tutorials

We provide step-by-step tutorials for our solvers and algorithms. Each tutorial demostrates the method's usage, beckground, and	 key-concepts.

Solver Tutorials:

- Gurobi/CPLEX: Comming Soon.
- COPT: Comming Soon.
- SCIP: Comming Soon.

Algorithm Tutorials:

- VCA: Our tutorial for the Variational Classical Annealing algorithm found in `src/tutorials/VCA`
- MCPG: Comming Soon.
- ECO-DQN: Comming Soon.

## File Structure

```
    ├── docs/       : ReadTheDocs website containing algorithms, tutorials, and dataset overview. 
    |
    └── src/
        ├── algorithms/
        |   ├── vca/       : Variational Classical Annealing algorithm.
        |   ├── mcpg/      : Monte Carlo Policy Gradient algorithm for Ising models.
        |   └── vta/       : Variational Transformer Annealing algorithm, Tranformer model VCA.
        |   
        ├── baseline/
        |   ├── gurobi.py  : Gurobi MIP Solver for Ising model.
        |   ├── cplex.py   : IBM ILOG CPLEX MIP Solver for Ising model.
        |   └── copt.py    : COPT Cardinal MIP Solver for Ising model.
        |
        ├── tutorials/
        |   ├── VCA/       : VCA tutorial for EA Ising models.
        |   ├── MCPG/      : MCPG tutorial, coming soon.
        |   └── ECO/       : ECO-DQN tutorial, coming soon.
        |
        └── envs/          : Conda environment files for algorithms.
```

## Reference

[Levy Lin, Zhiyuan Wang, Holden Mac Entee, Xingjian Zhao, and Xiao-Yang Liu.
*Reinforcement Learning for Ising Models: Datasets and Benchmark*,
NeurIPS ML4PS Workshop, 2025.](https://ml4physicalsciences.github.io/2025/files/NeurIPS_ML4PS_2025_245.pdf)
