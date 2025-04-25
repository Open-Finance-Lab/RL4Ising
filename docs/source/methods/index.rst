===================================
Reinforcement Algorithm/Methods
===================================

.. contents:: Table of Contents
   :local:


Exploratory Combinatorial Optimization with Reinforcement Learning (ECO-DQN)
==================================================================================

**Citation:**
Barrett, T. D., Clements, W. R., Foerster, J. N., & Lvovsky, A. I. (2019). *Exploratory Combinatorial Optimization with Reinforcement Learning*. In Proc. of the Thirty-Fourth AAAI Conference on Artificial Intelligence (AAAI-20). DOI: `10.1609/aaai.v34i04.5723 <https://doi.org/10.1609/aaai.v34i04.5723>`_

Overview
--------
ECO-DQN introduces a reinforcement learning framework for solving combinatorial optimization problems with a key focus on *reversible exploration*. The method allows agents to revise earlier decisions during inference, leading to more robust solutions.

Strengths
---------

- **Reversible Exploration**:
  The agent is permitted to undo prior actions and iteratively refine the solution. This mechanism enables it to escape local optima during test time.

- **Flexible Initialization**:
  ECO-DQN supports initialization from various strategies (e.g., random, greedy, heuristic) and can improve upon them. This makes it compatible with other optimization approaches.

Weaknesses
----------

- **High Computational Cost**:
  Each step in the decision process requires two inferences from a graph neural network—one for adding and one for removing actions. This leads to significantly longer per-instance runtimes compared to greedy methods.

- **Stopping Criterion Ambiguity**:
  Since the agent continues exploring during inference, determining when to stop (balancing runtime and solution quality) is challenging.

- **Outdated Algorithmic Core**:
  The approach uses Q-learning with experience replay and target networks to approximate the Q-function. While stabilizing, it incurs high sample complexity and is prone to training instability.




Monte Carlo Policy Gradient with Local Search (MCPG)
=====================================================

**Citation:**
Chen, C., Chen, R., Li, T., Ao, R., & Wen, Z. (2023). *A Monte Carlo Policy Gradient Method with Local Search for Binary Optimization*. arXiv:2307.00783.

Overview
--------
MCPG combines Monte Carlo policy gradient methods with local search techniques to address binary combinatorial optimization problems. It incorporates MCMC-based sampling and a theoretically justified convergence mechanism.

Strengths
---------

- **Efficient, Diverse Exploration**:
  Parallel MCMC sampling introduces both diversity and coherence in exploring the discrete solution space. This results in low-variance gradient estimates and fast convergence to high-quality solutions.

- **Theoretical Convergence Guarantee**:
  MCPG minimizes KL divergence to the Gibbs distribution and employs MCMC concentration inequalities, ensuring provable convergence in expectation to a stationary policy.

Weaknesses
----------

- **Ambiguous Stopping Criterion**:
  Similar to ECO-DQN, MCPG continues to explore during inference. Determining when additional sampling no longer improves results remains a practical challenge.



Revisiting Sampling for Combinatorial Optimization (iSCO)
==========================================================

**Citation:**
Sun, H., Goshvadi, K., Nova, A., Schuurmans, D., & Dai, H. (2023). *Revisiting Sampling for Combinatorial Optimization*. In Proceedings of the 40th International Conference on Machine Learning (PMLR 202:32859–32874).

Overview
--------
iSCO is a sampling-based optimization framework that utilizes parallel, gradient-based updates to perform efficient exploration over large neighborhoods, targeting hard combinatorial optimization problems.

Strengths
---------

- **Parallel, Gradient-Based Exploration**:
  By estimating neighborhood energy ratios via a single gradient and performing parallel updates, iSCO exploits hardware acceleration to achieve highly efficient sampling.

- **Strong Speed–Quality Trade-off**:
  Empirical results on tasks such as vertex cover, graph partitioning, and routing show that iSCO frequently outperforms or matches both prior learning-based methods and commercial solvers—often within a fraction of their runtimes.

Weaknesses
----------

- **High Iteration Counts on Some Tasks**:
  For complex problems like balanced graph partitioning, iSCO may require up to 800,000 sampling steps to achieve comparable results to specialized solvers, resulting in multi-minute runtimes.





Variational Neural Annealing (VCA)
===================================

**Citation:**
Hibat-Allah, M., Inack, E. M., Wiersema, R., Melko, R. G., & Carrasquilla, J. (2021). *Variational neural annealing*. Nature Machine Intelligence, 3(11), 952-961.

Overview
--------
VCA is a variational framework that applies neural sampling techniques—particularly autoregressive models—to approximate Boltzmann-like distributions and perform combinatorial optimization via annealing dynamics.

Strengths
---------

- **Autoregressive Sampling for Exploration**:
  The use of autoregressive neural networks allows VCA to flexibly explore the solution space and avoid common traps of static distributions.

Weaknesses
----------

- **Inductive Bias in Target Distribution**:
  By focusing on approximating the Boltzmann distribution, VCA imposes a strong modeling bias that may not align with optimal or problem-specific objectives.




REINFORCE Algorithm 
====================================

Overview
--------