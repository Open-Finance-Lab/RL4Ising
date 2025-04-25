.. _gurobi:

Gurobi Solver
=============

**Citation:**  
.. [Gurobi2024] Gurobi Optimization, LLC. (2024). *Gurobi Optimizer Reference Manual* (Version 11.0). Available at: https://www.gurobi.com

Overview
--------
Gurobi is a state-of-the-art commercial solver for linear, quadratic, and mixed-integer programming.  
In this project, we use Gurobi to solve the Max-Cut problem by formulating it as a **Quadratic Unconstrained Binary Optimization (QUBO)** problem — a special case of mixed-integer quadratic programming (MIQP) involving only binary variables and no explicit constraints.

Strengths
---------

- **Advanced Parallel Cut Generation**  
  Gurobi leverages automatic cutting-plane generation, heuristics, and parallel branch-and-bound tree search, significantly speeding up convergence for dense binary quadratic problems.

- **Optimality Guarantee**  
  Gurobi uses a branch-and-cut framework to provide certificates of global optimality for QUBO formulations, ensuring exact solutions whenever feasible.

Weaknesses
----------

- **Formulation Overhead**  
  Although QUBO models are compact, auxiliary transformations (e.g., symmetrization or scaling) may affect numerical stability and solver efficiency.

- **Scalability Limitations on Large Instances**  
  For large graphs (e.g., G70 with \(\|V\| = 10,000\)), Gurobi may require extended runtimes to close the optimality gap.  
  For example, it found a cut of 9490 in 0.5 hours and 9506 in 1 hour, illustrating challenges under tight runtime budgets.
