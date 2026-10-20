=============================
Task 2: RL4Ising
=============================

RL4Ising is a task that challenges you to build agents designed to search for the ground state of Ising models and surpass industry-level MIP solvers. 
Your mission: trains agents to effectively navigate the huge discrete space of Spin-Glass Ising models and to search for the ground state. 
This task builds upon RL4Maxcut --- an integration of Physics and RL designed for real-world scientific applications.

Task Overview
-----------------------

In this task, participants are invited to develop ground state agents to obtain high quality solutions and improve the scalability or performance of RL algorithms. We provide a solver baseline, inviting participants to beat or match the baseline results. Participants can explore a variety of avenues, including but not limited to:

- Improve Boltzmann Distribution sampling ; upgrade sampling speed or overcoming memory constraints
- Apply filter functions, such as, Local Search or Simulated Annealing.
- Explore and innovate RL algorithms, such as, MCPG, VCA, ECO-DQN.
- Design a Curriculm Learning schedule for more efficient exploration and faster convergance.

Participants are encouraged to propose creative improvements and extensions that further advance the search for the ground state.

Datasets
----------------------------

Here we curate a **challenging** instance-wise Spin Glass dataset featuring geometric frustration, large edge weights, large scale, and high dimensionality.

- **Geometric frustration**: Not all interactions can exist in their lowest energy state (There may be several orientations that reach the same energy level).
- **Large edge weights**: The numerical value of edge weightings can reach several hundred thousand.
- **Large scale**: Graphs containing hundreds or thousands of nodes and tens of thousands of edges.
- **High dimensionality**: Each node has many features associated with it. 

1D Spin Glass Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. csv-table::
   :file: ../_data/competition/ising/instances/spin_glass_1d.csv
   :widths: 25 25 25 45 45 75 25
   :header-rows: 1

2D Spin Glass Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. csv-table::
   :file: ../_data/competition/ising/instances/spin_glass_2d.csv
   :widths: 25 25 25 45 45 75 25
   :header-rows: 1

3D Spin Glass Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. csv-table::
   :file: ../_data/competition/ising/instances/spin_glass_3d.csv
   :widths: 25 25 25 45 45 75 25
   :header-rows: 1
..
    * - EA
    - 1
    - 4,312
    - 8,787
    - -0.9999327124518298 --- 0.9997497212906203
    - `https://zenodo.org/records/14578166 <https://zenodo.org/records/14578166>`_
    - [5]_
   * - EA
     - 3
     - 512
     - 1,536
     - -3.8221474911073994 --- 3.699167050468019
     - `https://zenodo.org/records/7562380 <https://zenodo.org/records/7562380>`_
     - [2]_

4D Spin Glass Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. csv-table::
   :file: ../_data/competition/ising/instances/spin_glass_4d.csv
   :widths: 25 25 25 45 45 75 25
   :header-rows: 1

Starter Kit 
----------------------------------------

This `starter kit <https://github.com/Open-Finance-Lab/RLSolver_Contest_2025>`_ includes training scripts and environment files for the Ising model. Follow the instructions below to get started.

Commands
~~~~~~~~~~~~~~~

To run the various methods, follow the commands listed below:

.. list-table::
   :widths: 25 25 25
   :header-rows: 1

   * - Method
     - Description
     - Command
   * - MCPG
     - Monte Carlo Policy Gradient
     - N/A
   * - ECO-DQN
     - Exploratory Combinatorial Optimization Deep Q-Network
     - N/A
   * - Gurobi
     - Mixed Integer Programming
     - N/A

:ref:`Benchmark <isingbenchmark>`
------------------------------------

Full benchmark can be found here, :ref:`Benchmark <isingbenchmark>`.

Baseline Solvers:

- `Gurobi <https://www.gurobi.com/faqs/mip-solvers/>`_: A mixed-integer programming solver that identifies optimal solutions given an objective function, typically by applying a branch-and-cut algorithm.

.. - cuLoRADS: GPU accelerated solver that combines the Burer-Monterio method and a splitting scheme with a logarithmic rank. [6]_

RL Methods:

- MCPG: Parallel MCMC sampling and a filter scheme to replace the objective function with one with a local search technique. [6]_

Metrics
-------

We will be evaluating scores based on the Hamiltonian (shown below) of the solution obtained. In other words, you are aiming to find the ground state configuration of an Ising model system. Your goal: achieve the lowest energy configuration.

.. math::
    E = -J \sum_{i<j}s_i s_j

To confirm submitted scores, we will be requiring submission with the encoded bit configuration as well as the reported score. 

**References**

.. [1] Hibat-Allah, M., Inack, E.M., Wiersema, R. et al. Variational neural annealing. Nat Mach Intell 3, 952–961 (2021). https://doi.org/10.1038/s42256-021-00401-3

.. [2] Fan, C., Shen, M., Nussinov, Z. et al. Searching for spin glass ground states through deep reinforcement learning. Nat Commun 14, 725 (2023). https://doi.org/10.1038/s41467-023-36363-w

.. [3] Mills, K., Ronagh, P. & Tamblyn, I. Finding the ground state of spin Hamiltonians with reinforcement learning. Nat Mach Intell 2, 509–517 (2020). https://doi.org/10.1038/s42256-020-0226-x

.. [4] Wiegele, A. (2007, September). Biq Mac Library: A collection of Max-Cut and quadratic 0–1 programming instances of medium size [Data set]. Alpen-Adria-Universität Klagenfurt. http://biqmac.uni-klu.ac.at/biqmaclib.html

.. [5] Zhang, H., and Kamenev, A. 2025. On Computational Complexity of 3D Ising Spin Glass: Lessons from D-Wave Annealer. arXiv e-prints, p.arXiv:2501.01107.

.. [6]_ Han, Q., Lin, Z., Liu, H., Chen, C., Deng, Q., Ge, D., & Ye, Y. (2024). Accelerating low-rank factorization-based semidefinite programming algorithms on GPU. arXiv. https://arxiv.org/abs/2407.15049

.. [6] Chen, C., Chen, R., Li, T., Ao, R., & Wen, Z. (2023). Monte Carlo policy gradient method for binary optimization. arXiv. https://arxiv.org/abs/2307.00783