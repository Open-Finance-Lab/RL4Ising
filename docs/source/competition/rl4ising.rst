=============================
Task 2: RL4Ising
=============================

RL4Ising is a task that challenges you to build agents designed to search for the ground state of Ising models and surpass industry-level MIP solvers. 
Your mission: trains agents to effectively navigate the huge discrete space of Spin-Glass Ising models to search for the ground state, while overcoming complexities from scale and dimensionality. 
This task builds upon RL4Maxcut --- an integration of Physics and RL designed for real-world scientific applications.

Task Overview
-----------------------

In this task, participants are invited to develop ground state agents capable of obtaining high quality solutions and feature improved scalbility or performance than industry-level solvers. 
Participants can explore a variety of avenues, including but not limited to:

- Improve Boltzmann Distribution sampling ; upgrade sampling speed for high quality samples or upgrade memory constraints for high dimensionality 
- Apply filter functions, such as, Local Search or Simulated Annealing.
- Explore and innovate RL algorithms, such as, MCPG, VCA, ECO-DQN.
- Design a Curriculm Learning schedule for more efficient exploration and faster convergance.

Participants are encouraged to propose creative improvements and extensions that further advance the search for the ground state.

Datasets
----------------------------

1D Spin Glass Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
   :widths: 25 25 25 75 25
   :header-rows: 1

   * - Instance
     - \# of Instances
     - \# of Spins
     - Url
     - Reference
   * - Chain
     - 6
     - 300
     - `https://biqmac.aau.at/library/mac/ising/ <https://biqmac.aau.at/library/mac/ising/>`_
     - [4]
   * - Chain
     - 6
     - 250
     - `https://biqmac.aau.at/library/mac/ising/ <https://biqmac.aau.at/library/mac/ising/>`_
     - [4]
   * - Chain
     - 6
     - 200
     - `https://biqmac.aau.at/library/mac/ising/ <https://biqmac.aau.at/library/mac/ising/>`_ 
     - [4]
   * - Chain
     - 6
     - 150
     - `https://biqmac.aau.at/library/mac/ising/ <https://biqmac.aau.at/library/mac/ising/>`_ 
     - [4]
   * - Chain
     - 6
     - 100
     - `https://biqmac.aau.at/library/mac/ising/ <https://biqmac.aau.at/library/mac/ising/>`_ 
     - [4]

2D Spin Glass Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
   :widths: 25 25 25 75 25
   :header-rows: 1

   * - Instance
     - \# of Instances
     - \# of Spins
     - Url
     - Reference
   * - EA
     - 3
     - 1,600
     - `https://github.com/VectorInstitute/VariationalNeuralAnnealing?tab=readme-ov-file <https://github.com/VectorInstitute/VariationalNeuralAnnealing?tab=readme-ov-file>`_
     - [1]
   * - EA
     - 3
     - 900
     - `https://zenodo.org/records/3897413 <https://zenodo.org/records/3897413>`_
     - [2]
   * - Spin-Glass
     - 3
     - 256
     - `https://zenodo.org/records/7562380 <https://zenodo.org/records/7562380>`_
     - [3]

3D Spin Glass Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
   :widths: 25 25 25 75 25
   :header-rows: 1

   * - Instance
     - \# of Instances
     - \# of Spins
     - Url
     - Reference
   * - EA
     - 1
     - 4,644
     - `https://zenodo.org/records/14578166 <https://zenodo.org/records/14578166>`_
     - [5]
   * - EA
     - 1
     - 4,312
     - `https://zenodo.org/records/14578166 <https://zenodo.org/records/14578166>`_
     - [5]
   * - EA
     - 3
     - 1,000
     - `https://zenodo.org/records/3897413 <https://zenodo.org/records/3897413>`_
     - [2]
   * - EA
     - 3
     - 512
     - `https://zenodo.org/records/3897413 <https://zenodo.org/records/3897413>`_
     - [2]

4D Spin Glass Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
   :widths: 25 25 25 75 25
   :header-rows: 1

   * - Instance
     - \# of Instances
     - \# of Spins
     - Url
     - Reference
   * - EA
     - 3
     - 4,096
     - `https://zenodo.org/records/3897413 <https://zenodo.org/records/3897413>`_
     - [2]
   * - EA
     - 3
     - 2,041
     - `https://zenodo.org/records/3897413 <https://zenodo.org/records/3897413>`_
     - [2]
   * - EA
     - 3
     - 1,296
     - `https://zenodo.org/records/3897413 <https://zenodo.org/records/3897413>`_
     - [2]
   * - EA
     - 3
     - 625
     - `https://zenodo.org/records/3897413 <https://zenodo.org/records/3897413>`_
     - [2]

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
     
**References**

.. [1] Hibat-Allah, M., Inack, E.M., Wiersema, R. et al. Variational neural annealing. Nat Mach Intell 3, 952–961 (2021). https://doi.org/10.1038/s42256-021-00401-3
.. [2] Mills, K., Ronagh, P. & Tamblyn, I. Finding the ground state of spin Hamiltonians with reinforcement learning. Nat Mach Intell 2, 509–517 (2020). https://doi.org/10.1038/s42256-020-0226-x
.. [3] Fan, C., Shen, M., Nussinov, Z. et al. Searching for spin glass ground states through deep reinforcement learning. Nat Commun 14, 725 (2023). https://doi.org/10.1038/s41467-023-36363-w
.. [4] Rendl, F., Rinaldi, G., & Wiegele, A. (2010). Solving Max-Cut to optimality by intersecting semidefinite and polyhedral relaxations. Mathematical Programming, 121(2), 307.
.. [5] Zhang, H., and Kamenev, A. 2025. On Computational Complexity of 3D Ising Spin Glass: Lessons from D-Wave Annealer. arXiv e-prints, p.arXiv:2501.01107.