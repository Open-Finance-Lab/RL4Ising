.. _qaoa:

Resource-Efficient QAOA for Max-Cut
====================================

**Citation:**
Wurtz, G. A., & Love, P. J. (2021). *Resource Efficient QAOA for Max-Cut*. npj Quantum Information, 7, 82.

Overview
--------
This variant of the Quantum Approximate Optimization Algorithm (QAOA) is tailored for near-term quantum computers (NISQ) by minimizing circuit depth and reducing entangling gate operations, enabling more feasible deployment on noisy hardware.

Strengths
---------

- **NISQ-Friendly Implementation**:
  The reduced circuit depth and entanglement requirements help mitigate decoherence and gate noise, making this algorithm more practical on today’s quantum devices.

Weaknesses
----------

- **Classical Preprocessing Overhead**:
  Efficient implementation depends on identifying commuting operator groups via graph coloring or partitioning, which is itself computationally expensive for large or dense graphs.

- **Dependency on Graph Structure**:
  The benefits of resource efficiency are most prominent on sparse or low-degree graphs. In dense or fully connected graphs, the number of commuting terms decreases, diminishing performance advantages.