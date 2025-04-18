==================================
Instances of Ising Models Overview
==================================

.. contents:: Table of Contents
   :local:

Description
===========
Our dataset collection spans a diverse set of spin systems that are central to both statistical physics and combinatorial optimization. These instances serve as benchmarks for algorithms tackling complex energy landscapes. Below is a high-level introduction to the core instance types and how we organize our datasets.

Categories of Ising Models
--------------------------

:doc:`Ferromagnetic Ising Models <ferromagnetism>`:
These instances represent one of the simplest yet most fundamental systems in statistical mechanics. In ferromagnetic configurations, all spins prefer to align in the same direction, minimizing the system's energy. They exhibit critical behavior such as phase transitions and are widely used in benchmarking due to their well-understood structure.

:doc:`Spin Glasses <spin_glass>`:
Spin glass systems are characterized by disorder and frustration — a scenario in which spins interact with conflicting constraints that cannot all be simultaneously satisfied. These models are difficult to optimize due to their intricate energy landscapes, making them ideal benchmarks for advanced optimization algorithms such as reinforcement learning, quantum annealing, and simulated annealing.

:doc:`Spin Ice <spin_ice>`:
Inspired by the arrangement of protons in ice, spin ice models mimic "ice rules" in spin configurations, leading to emergent quasiparticle behavior and exotic magnetic monopole excitations. These models are of great interest in condensed matter physics and have recently gained traction in programmable quantum simulators and artificial materials.


Dataset Categorization
-----------------------

To facilitate benchmarking across different complexity levels and problem types, we partition each Ising model type into **three subcategories**:

- **Simple**  
  Instances with fewer than 256 spins. These systems are small enough for exhaustive methods or exact solvers and often have regular or predictable interaction patterns.

- **Intermediate**  
  Instances with between 256 and 1023 spins. These are more challenging due to increased size or interaction complexity. They are well-suited for testing heuristic or hybrid quantum-classical methods.

- **Complex**  
  Instances with 1024 spins or more. These often represent high-dimensional spin glasses or large-scale simulations of physical systems. They pose significant challenges for both classical and quantum solvers, making them important benchmarks for state-of-the-art techniques in physics and optimization.