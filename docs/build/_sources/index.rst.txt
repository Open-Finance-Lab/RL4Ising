.. Reinforcement Learning for Ising Problem documentation master file, created by
   sphinx-quickstart on Tue Jan 21 19:38:31 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==============================================================================================
Welcome to `Reinforcement Learning for Ising Model <https://github.com/YangletLiu/RL4Ising>`_!
==============================================================================================

.. Add your content using ``reStructuredText`` syntax. See the
   `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
   documentation for details.

`Reinforcement Learning for Ising Model <https://github.com/YangletLiu/RL4Ising>`_ is an open-source dataset of Ising models and benchmark of SOTA ground state Reinforcement Learning methods. 
Our goal is to document the progress of current and future RL methods at searching for the ground state of Ising model in different scale, dimensionality, and Ising model classifications

Reinforcement Learning for Ising model provides a **collective dataset**, **solver baseline**, **SOTA RL tutorials**, and **RL benchmark** :

   - **Collective Dataset**: Over 190,000 synthetic or real Ising model instances spanning 3 classifications.
   - **Solver Baseline**: Industry-level commerical and open-source MIP solvers
   - **SOTA RL Tutorials**: ...
   - **RL Benchmark**: ... 


.. toctree::
   :maxdepth: 1
   :hidden:

   Home <self>

.. toctree::
   :maxdepth: 1
   :caption: Overview

   overview/key_concepts
   overview/motivation
   overview/content

.. toctree::
   :maxdepth: 1
   :caption: Datasets

   datasets/classification
   datasets/spin_glass
   datasets/spin_ice
   datasets/ferromagnetic
   datasets/anti_ferromagnetic

.. toctree::
   :maxdepth: 1
   :caption: Baseline Solvers

   solvers/gurobi
   solvers/cplex
   solvers/copt
   solvers/scip

.. toctree::
   :maxdepth: 1
   :caption: RL Algorithms

   methods/s2v
   methods/vca
   methods/mcpg
   methods/reinforce

.. toctree::
   :maxdepth: 1
   :caption: Benchmarks

   benchmark/results

.. toctree::
   :maxdepth: 1
   :caption: RL4Ising Competition 2025

   competition/overview
   competition/rl4maxcut
   competition/rl4ising

.. toctree::
   :maxdepth: 1
   :caption: References

   references/dataset_references


