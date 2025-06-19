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
