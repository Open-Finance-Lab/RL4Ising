==========
Spin Glass
==========

Description of Ising Model Type
===============================

A spin glass Ising model is characterized by frustrated interactions, meaning some neighboring spins prefer to align while others prefer to oppose. These conflicting orientations prevent the system from reaching a uniformly ordered state.
The energy configuration of this model can be given by

.. math::
    E = -J \sum_{<i,j>}s_i s_j

Here, :math:`J_{<i,j>}` can be either positive or negative. If :math:`J_{<i,j>}` is positive, :math:`s_i` and :math:`s_j` prefer to align and, conversely, they will anti-align. This is the precise phenomenon that defines a spin glass.

Instances
=========

The instances we are providing for the spin glass Ising model type consist of weighted edges. Note that there are both positive and negative edge weights. The complexity of an instance is determined not only by the size, but also the pattern of interactions and frustration.

.. image:: /_static/spin_glass_figure_simple.png
    :align: center

.. raw:: html

    <div style="height: 40px;"></div>

.. image:: /_static/spin_glass_figure_intermediate.png
    :align: center

.. raw:: html

    <div style="height: 40px;"></div>

.. image:: /_static/spin_glass_figure_complex.png
    :align: center
