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

Here we curate a **challenging** Spin Glass dataset featuring goemetric frustration, large edge weights, large scale, and high dimensionality.

- **Geometric frustration**: Not all interactions can exist in their lowest energy state (There may be several orientations that reach the same energy level).
- **Large edge weights**: The numerical value of edge weightings can reach several hundred thousand.
- **Large scale**: Graphs containing hundreds or thousands of nodes and tens of thousands of edges.
- **High dimensionality**: Each node has many features associated with it. 

1D Spin Glass Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
   :widths: 25 25 25 45 75 25
   :header-rows: 1

   * - Instance
     - \# of Instances
     - \# of Spins
     - Coupling Strength
     - Url
     - Reference
   * - Chain
     - 6
     - 300
     - -244104.0 --- 210331.0
     - `https://biqmac.aau.at/library/mac/ising/ <https://biqmac.aau.at/library/mac/ising/>`_
     - [4]_
   * - Chain
     - 6
     - 250
     - -193801.0 --- 277406.0
     - `https://biqmac.aau.at/library/mac/ising/ <https://biqmac.aau.at/library/mac/ising/>`_
     - [4]_
   * - Chain
     - 6
     - 200
     - -231636.0 --- 239764.0
     - `https://biqmac.aau.at/library/mac/ising/ <https://biqmac.aau.at/library/mac/ising/>`_ 
     - [4]_
   * - Chain
     - 6
     - 150
     - -219729.0 --- 182372.0
     - `https://biqmac.aau.at/library/mac/ising/ <https://biqmac.aau.at/library/mac/ising/>`_ 
     - [4]_
   * - Chain
     - 6
     - 100
     - -212231.0 --- 239752.0
     - `https://biqmac.aau.at/library/mac/ising/ <https://biqmac.aau.at/library/mac/ising/>`_ 
     - [4]_

2D Spin Glass Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
   :widths: 25 25 25 45 75 25
   :header-rows: 1

   * - Instance
     - \# of Instances
     - \# of Spins
     - Coupling Strength
     - Url
     - Reference
   * - EA
     - 3
     - 1,600
     - -0.9997712503653102 --- 0.9997515751485249
     - `https://github.com/VectorInstitute/VariationalNeuralAnnealing?tab=readme-ov-file <https://github.com/VectorInstitute/VariationalNeuralAnnealing?tab=readme-ov-file>`_
     - [1]_
   * - EA
     - 3
     - 900
     - -3.768221414584132 --- 3.146263619470661
     - `https://zenodo.org/records/7562380 <https://zenodo.org/records/7562380>`_
     - [2]_
   * - Spin-Glass
     - 3
     - 256
     - -4.108692623805201 --- 2.79308500014654
     - `https://zenodo.org/records/3897413 <https://zenodo.org/records/3897413>`_
     - [3]_

3D Spin Glass Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
   :widths: 25 25 25 45 75 25
   :header-rows: 1

   * - Instance
     - \# of Instances
     - \# of Spins
     - Coupling Strength
     - Url
     - Reference
   * - EA
     - 1
     - 4,644
     - -0.9998457617927303 --- 0.9997514748439584
     - `https://zenodo.org/records/14578166 <https://zenodo.org/records/14578166>`_
     - [5]_
   * - EA
     - 1
     - 4,312
     - -0.9999327124518298 --- 0.9997497212906203
     - `https://zenodo.org/records/14578166 <https://zenodo.org/records/14578166>`_
     - [5]_
   * - EA
     - 3
     - 1,000
     - -4.324181919314443 --- 3.473301731916228
     - `https://zenodo.org/records/7562380 <https://zenodo.org/records/7562380>`_
     - [2]_
   * - EA
     - 3
     - 512
     - -3.8221474911073994 --- 3.699167050468019
     - `https://zenodo.org/records/7562380 <https://zenodo.org/records/7562380>`_
     - [2]_

4D Spin Glass Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
   :widths: 25 25 25 45 75 25
   :header-rows: 1

   * - Instance
     - \# of Instances
     - \# of Spins
     - Coupling Strength
     - Url
     - Reference
   * - EA
     - 3
     - 4,096
     - -3.974500095603923 --- 4.07455276849542
     - `https://zenodo.org/records/7562380 <https://zenodo.org/records/7562380>`_
     - [2]_
   * - EA
     - 3
     - 2,041
     - -4.570368670534508 --- 3.942823083195053
     - `https://zenodo.org/records/7562380 <https://zenodo.org/records/7562380>`_
     - [2]_
   * - EA
     - 3
     - 1,296
     - -5.094655883484119 --- 3.8885579774279107
     - `https://zenodo.org/records/7562380 <https://zenodo.org/records/7562380>`_
     - [2]_
   * - EA
     - 3
     - 625
     - -3.824305097349775 --- 3.525499579857149
     - `https://zenodo.org/records/7562380 <https://zenodo.org/records/7562380>`_
     - [2]_

Starter Kit 
----------------------------------------

This `starter kit <https://github.com/HMacEntee/RL4Ising_Contest_2025>`_ includes training scripts and environment files for the Ising model. Follow the instructions below to get started.

Commands
--------

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
   * - VCA
     - Variational Classical Annealing
     - N/A
   * - Gurobi
     - Mixed Integer Programming
     - N/A

Benchmark
-----------------------

Baseline Solvers:
- Gurobi
- cuLoRADS

RL Methods:
- MCPG

**References**

.. [1] Hibat-Allah, M., Inack, E.M., Wiersema, R. et al. Variational neural annealing. Nat Mach Intell 3, 952–961 (2021). https://doi.org/10.1038/s42256-021-00401-3
.. [2] Fan, C., Shen, M., Nussinov, Z. et al. Searching for spin glass ground states through deep reinforcement learning. Nat Commun 14, 725 (2023). https://doi.org/10.1038/s41467-023-36363-w
.. [3] Mills, K., Ronagh, P. & Tamblyn, I. Finding the ground state of spin Hamiltonians with reinforcement learning. Nat Mach Intell 2, 509–517 (2020). https://doi.org/10.1038/s42256-020-0226-x
.. [4] Rendl, F., Rinaldi, G., & Wiegele, A. (2010). Solving Max-Cut to optimality by intersecting semidefinite and polyhedral relaxations. Mathematical Programming, 121(2), 307.
.. [5] Zhang, H., and Kamenev, A. 2025. On Computational Complexity of 3D Ising Spin Glass: Lessons from D-Wave Annealer. arXiv e-prints, p.arXiv:2501.01107.