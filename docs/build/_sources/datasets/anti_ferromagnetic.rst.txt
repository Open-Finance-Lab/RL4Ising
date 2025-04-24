==================
Anti-Ferromagnetic
==================

Description of Ising Model Type
===============================

In an anti-ferromagnetic Ising model, neighboring spins want to anti-align. In other words, they want to point in the opposite directions to minimize the system's energy.
The energy configuration of this model can be given by

.. math::
    E = -J \sum_{<i,j>}s_i s_j

If the neighboring spins point in the same direction, the energy of the system will increase and, conversely arranged, will decrease. 

Instances
=========

The instances we are providing for the anti-ferromagnetic Ising model type consist of weighted edges. Note that there are only negative weights present for these instances. The complexity of an instance is determined by its size (# of nodes).

2D
-----------
.. image:: /_static/anti-ferromagnetism_2D.png
    :align: center

