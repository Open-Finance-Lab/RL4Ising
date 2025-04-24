.. _isco:

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