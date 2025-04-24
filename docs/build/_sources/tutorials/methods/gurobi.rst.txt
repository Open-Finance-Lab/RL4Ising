.. _gurobi:

Gurobi Solver
=============

**Citation:**
Gurobi Optimization, LLC. (Latest Release). *Gurobi Optimizer Reference Manual*.

Overview
--------
Gurobi is a state-of-the-art commercial solver for linear, quadratic, and mixed-integer programming. It solves the Max-Cut problem by formulating it as a mixed-integer quadratic program (MIQP) or via linearized approximations.

Strengths
---------

- **Advanced Parallel Cut Generation**:
  Gurobi applies automatic cutting-planes, heuristics, and parallel tree-search threads at each node, accelerating convergence on dense MIP problems.

- **Optimality Guarantee**:
  Using branch-and-cut, Gurobi provides certificates of global optimality for the Max-Cut formulation, ensuring exact solutions when possible.

Weaknesses
----------

- **Formulation Overhead**:
  Encoding Max-Cut as a QUBO or MIP often requires auxiliary variables and linearization constraints. These overheads can significantly inflate the model size and slow root-node relaxation.

- **Scalability Limits on Large Instances**:
  On large-scale benchmarks (e.g., G70 with \|V\| = 10,000), Gurobi may take substantial time to close the optimality gap. While it found a cut of 9490 in 0.5h and 9506 in 1h, these results highlight potential bottlenecks under time constraints.