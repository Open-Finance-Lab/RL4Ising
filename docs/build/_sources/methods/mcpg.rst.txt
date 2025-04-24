.. _mcpg:

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