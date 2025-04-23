.. _eco_dqn:

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
