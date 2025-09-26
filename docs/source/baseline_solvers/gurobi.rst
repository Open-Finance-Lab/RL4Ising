=======================
Gurobi Solver
=======================

**Citation:**
Gurobi Optimization, LLC. (Latest Release). *Gurobi Optimizer Reference Manual*.

Overview
========
Gurobi is a state-of-the-art commercial solver for linear, quadratic, and mixed-integer programming. It solves the Max-Cut problem by formulating it as a mixed-integer quadratic program (MIQP) or via linearized approximations.

Strengths
=========

- **Advanced Parallel Cut Generation**:
  Gurobi applies automatic cutting-planes, heuristics, and parallel tree-search threads at each node, accelerating convergence on dense MIP problems.

- **Optimality Guarantee**:
  Using branch-and-cut, Gurobi provides certificates of global optimality for the Max-Cut formulation, ensuring exact solutions when possible.

Weaknesses
==========

- **Formulation Overhead**:
  Encoding Max-Cut as a QUBO or MIP often requires auxiliary variables and linearization constraints. These overheads can significantly inflate the model size and slow root-node relaxation.

- **Scalability Limits on Large Instances**:
  On large-scale benchmarks (e.g., G70 with \|V\| = 10,000), Gurobi may take substantial time to close the optimality gap. While it found a cut of 9490 in 0.5h and 9506 in 1h, these results highlight potential bottlenecks under time constraints.

<<<<<<< HEAD:docs/source/solvers/index.rst
IBM CPLEX Solver
======================

**Citation:**
Cplex, I. I. (2009). V12. 1: User’s Manual for CPLEX. International Business Machines Corporation, 46(53), 157.

Mosek Solver
===================

**Citation:**
https://docs.mosek.com/latest/pythonfusion/index.html

COPT Solver
===============

**Citation:**
https://doi.org/10.48550/arXiv.2208.14314

Ecole Solver
======================

**Citation:**
Antoine Prouvost, Justin Dumouchelle, Lara Scavuzzo, Maxime Gasse, Didier Chetelat, & Andrea Lodi (2020). Ecole: A Gym-like Library for Machine Learning in Combinatorial Optimization Solvers. In Learning Meets Combinatorial Algorithms at NeurIPS2020.

SCIP Solver 
======================

**Citation:**
Suresh Bolusani, Mathieu Besançon, Ksenia Bestuzheva, Antonia Chmiela, João Dionísio, Tim Donkiewicz, Jasper van Doornmalen, Leon Eifler, Mohammed Ghannam, Ambros Gleixner, Christoph Graczyk, Katrin Halbig, Ivo Hedtke, Alexander Hoen, Christopher Hojny, Rolf van der Hulst, Dominik Kamp, Thorsten Koch, Kevin Kofler, Jurgen Lentz, Julian Manns, Gioni Mexi, Erik~Mühmer, Marc E. Pfetsch, Franziska Schlosser, Felipe Serrano, Yuji Shinano, Mark Turner, Stefan Vigerske, Dieter Weninger, & Lixing Xu (2024). The SCIP Optimization Suite 9.0 [White paper]. Optimization Online.

RL4CO Solver
=====================

**Citation:**
https://doi.org/10.48550/arXiv.2306.17100
=======
Tutorial
===========
>>>>>>> b98a1f8 (website overhaul):docs/source/solvers/gurobi.rst
