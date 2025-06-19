==========================================
Task 1: RL4MaxCut
==========================================

RL4Maxcut is a task that challenges you to build agents capable of solving the MaxCut problem on unseen graphs drawn from diverse distributions, while surpassing industry-level MIP solvers in performance and scalability.  
Your mission: train agents to effectively explore the vast discrete space of graph partitions and generalize beyond the training set to new, previously unseen graph instances.  
This task emphasizes distribution-wise generalization — encouraging the development of agents that learn robust, transferable policies applicable to a wide range of graph types (e.g., ER, BA, PowerLaw), rather than overfitting to specific training graphs.


Task Overview
-----------------------

In this task, participants are invited to develop MaxCut agents that can produce high-quality solutions and improve the scalability and generalization of reinforcement learning algorithms. We provide a baseline solver, and invite participants to match or surpass its performance — particularly on previously unseen graphs drawn from diverse distributions.

Participants are encouraged to explore a wide range of approaches, including but not limited to:

- Improve sampling strategies, such as enhancing solution diversity, improving rollout efficiency, or reducing memory usage.
- Apply post-processing filters, such as Local Search or Simulated Annealing, to refine the output from RL agents.
- Explore and innovate RL algorithms, such as S2V-DQN, ECO-DQN.
- Design a Curriculum Learning schedule to gradually increase problem complexity and accelerate convergence.

Participants are encouraged to propose creative enhancements and hybrid methods that further advance the ability of RL agents to generalize to new and challenging MaxCut instances across different graph distributions.

Datasets
----------------------------
We provide a **challenging dataset** of graphs curated to evaluate the **distribution-wise generalization** of MaxCut agents. These graphs vary widely in both **structural properties** and **graph sizes**, encouraging models to learn transferable policies rather than overfit to specific instances.

Starter Kit 
----------------------------------------

This `starter kit <https://github.com/HMacEntee/RL4Ising_Contest_2025>`_ includes training scripts and environment files for the Maxcut problem. Follow the instructions below to get started.

Commands
--------

To run the various methods, follow the commands listed below:

.. list-table::
   :widths: 25 25 25
   :header-rows: 1

   * - Method
     - Description
     - Command
   * - MCPG
     - Monte Carlo Policy Gradient
     - N/A
   * - ECO-DQN
     - Exploratory Combinatorial Optimization Deep Q-Network
     - N/A
   * - Gurobi
     - Mixed Integer Programming
     - N/A

:ref:`Benchmark <benchmark>`
----------------------------

Baseline Solvers:

- `Gurobi <https://www.gurobi.com/faqs/mip-solvers/>`_: A mixed-integer programming solver that identifies optimal solutions given an objective function, typically by applying a branch-and-cut algorithm.


RL Methods:

- MCPG: Parallel MCMC sampling and a filter scheme to replace the objective function with one with a local search technique. [7]_
- ECO-DQN: Reinforcement learning method for MaxCut that trains on a distribution of graphs, using a graph neural network to embed states and learn Q-values that guide partition decisions.


Metrics:

Each solution is evaluated based on the cut size, which is the total weight of edges that are cut by the current node partition.
The goal is to maximize the cut value—i.e., find the node partition that produces the maximum total weight across the cut.
This is equivalent to finding the optimal solution to the MaxCut problem, and serves as the benchmark for comparing different solvers and algorithms.

**References**

.. [6] Han, Q., Lin, Z., Liu, H., Chen, C., Deng, Q., Ge, D., & Ye, Y. (2024). Accelerating low-rank factorization-based semidefinite programming algorithms on GPU. arXiv. https://arxiv.org/abs/2407.15049

.. [7] Chen, C., Chen, R., Li, T., Ao, R., & Wen, Z. (2023). Monte Carlo policy gradient method for binary optimization. arXiv. https://arxiv.org/abs/2307.00783
