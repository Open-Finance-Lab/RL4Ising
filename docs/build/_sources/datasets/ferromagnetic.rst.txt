===============================
Ferromagnetic Dataset
===============================

Description of Ising Model Type
===============================

In a ferromagnetic Ising model, neighboring spins want to align. In other words, they want to point in the same direction to minimize the system's energy. Uniformity, whether it be in the form of all spins pointing up or down, is a key trait of the ferromagnetic instance.
The energy configuration of this model can be given by

.. math::
    E = -J \sum_{<i,j>}s_i s_j

If the neighboring spins point in the same direction, the energy of the system will decrease and, conversely arranged, will increase. Essential behaviors of the ferromagnetic model are the randomness of spins at high temperatures, and the aligned spins at lower temperatures.  

Instances
=========

The instances we are providing for the ferromagnetic Ising model type consist of weighted edges. Note that there are only positive weights present for these instances. The complexity of an instance is determined by its size (# of nodes).

2D
-----------
.. list-table::
   :widths: 25 25 25 25 25 25
   :header-rows: 1

   * - Instance
     - \# of Instances
     - \# of Spins
     - Complexity
     - Graph Geometry
     - Reference
   * - Ferromagnetic
     - 10,000
     - 1,600
     - Complex
     - Metropolis
     - [13]_
   * - Ferromagnetic
     - 10,000
     - 1,600
     - Complex
     - Metropolis
     - [13]_
   * - Ferromagnetic
     - 10,000
     - 1,600
     - Complex
     - Metropolis
     - [13]_
   * - Ferromagnetic
     - 10,000
     - 1,600
     - Complex
     - Metropolis
     - [13]_
   * - Ferromagnetic
     - 10,000
     - 1,600
     - Complex
     - Metropolis
     - [13]_
   * - Ferromagnetic
     - 10,000
     - 1,600
     - Complex
     - Metropolis
     - [13]_
   * - Ferromagnetic
     - 10,000
     - 1,600
     - Complex
     - Metropolis
     - [13]_
   * - Ferromagnetic
     - 10,000
     - 1,600
     - Complex
     - Metropolis
     - [13]_
   * - Ferromagnetic
     - 10,000
     - 1,600
     - Complex
     - Metropolis
     - [13]_


Dataset References
===================

Below contain the references to the datasets we gathered on this website.

.. [13] P. Mehta, M. Bukov, C.-H. Wang, A.G. Day, C. Richardson, C.K. Fisher, D.J. Schwab. A high-bias, low-variance introduction to machine learning for physicists. Physics Reports, 810 (2019), pp. 1-124, 10.1016/j.physrep.2019.03.001


This textbook introduces Machine Learning and its applications towards physics problems and research. Within the textbook, contains an Ising model dataset of locally-connected 2D Ising models.

