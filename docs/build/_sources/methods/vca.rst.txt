.. _vca:

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