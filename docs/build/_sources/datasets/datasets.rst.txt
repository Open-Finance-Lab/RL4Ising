================
Datasets
================

Our dataset collection spans a diverse set of spin systems that are central to both statistical physics and combinatorial optimization. These instances serve as benchmarks for algorithms tackling complex energy landscapes. Below is a high-level introduction to the core instance types and how we organize our datasets.

Dataset Introduction
======================

To facilitate benchmarking across different complexity levels and problem types, we partition each Ising model type into **three subcategories**:

- **Simple**  
  Instances with fewer than 256 spins. These systems are small enough for exhaustive methods or exact solvers and often have regular or predictable interaction patterns.

- **Intermediate**  
  Instances with between 256 and 1023 spins. These are more challenging due to increased size or interaction complexity. They are well-suited for testing heuristic or hybrid quantum-classical methods.

- **Complex**  
  Instances with 1024 spins or more. These often represent high-dimensional spin glasses or large-scale simulations of physical systems. They pose significant challenges for both classical and quantum solvers, making them important benchmarks for state-of-the-art techniques in physics and optimization.

Instances of Ising Models
-----------------------------

.. image:: /_static/instances_model_figure.png
    :align: center

Note that there is additional information about the graph configurations present in our datasets in our Additional Resources section.

Datasets
============

.. toctree::
   :maxdepth: 2

   spin_glass
   spin_ice
   ferromagnetic
   anti_ferromagnetic
