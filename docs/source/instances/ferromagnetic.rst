=======================
Ferromagnetic Instances
=======================

Description of Ising Model Type
===============================

In a ferromagnetic Ising model, neighboring spins want to align. In other words, they want to point in the same direction to minimize the system's energy. Uniformity, whether it be in the form of all spins pointing up or down, is a key trait of the ferromagnetic instance.
The energy configuration of this model can be given by

.. math::
    E = -J \sum_{<i,j>}s_i s_j

If the neighboring spins point in the same direction, the energy of the system will decrease and, conversely arranged, will increase. Essential behaviors of the ferromagnetic model are the randomness of spins at high temperatures, and the aligned spins at lower temperatures.  

Instances
=========

The instances we are providing for the ferromagnetic Ising model type consist of weighted edges. Note that there are only positive weights present for these instances. The complexity of an instance is determined by its size (# of nodes). Also note that each graph geometry is explained in more detail in the :doc:`Graph Geometry<geometry>` subpage.

.. image:: /_static/ferromagnetism_figure.png
    :align: center

