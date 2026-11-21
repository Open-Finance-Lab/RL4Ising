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

Software Requirements for FOCI Cluster
--------------------------------------

- A100 - CUDA 11.4 or later supported
- tensorflow-2.12.0 (minimum version for CUDA 11.8)
- python 3.8-3.11

Minor compatibility is available for all versions within 11 meaning new code and old hardware versions should be supported with the right packages.

Sources:

- `VCA environment file <https://github.com/Open-Finance-Lab/RL4Ising/blob/main/src/envs/vca_environment.yaml>`_
- `TensorFlow GPU build configurations <https://www.tensorflow.org/install/source#gpu>`_
