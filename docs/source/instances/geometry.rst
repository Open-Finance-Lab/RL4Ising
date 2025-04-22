==============
Graph Geometry
==============

In this subpage we will explore the different graph geometries that may be present as Ising models. Note that all figures representing their designated graph geometry are arbitrary and for visualization purposes only.

Bi-Clique
=========

Cubic
=====

Cylindrical
===========

Diamond
=======

Edwards-Anderson (EA)
=====================

Full
====

The fully connected Ising model consists of a lattice where each node has a connection to every other node. For the purposes of our dataset, we have removed all edges that are reflexive, i.e., a node points to itself. Below is an image depicting a fully connected Ising model instance.

Hopfield
========

Line
====

The line Ising model allows at most two neighbors to each node. As a result, the Ising model chain can be graphically represented by a line of connected nodes. Below is an image depicting a 5-node line-connected Ising model instance.

.. image:: /_static/line_instance_graph.png
    :align: center

Sherrington-Kirkpatrick (SK)
============================

Toroidal
========

A toroidal Ising model contains a lattice with periodic boundary conditions. The criterion for the boundary conditions are as follows:

1) The left edge is adjcaent to the right edge.

2) The top edge is adjacent to the bottom edge.

These conditions create a surface that has no boundaries. In other words, it ensures every spin has the same number of neighors. The image below depicts a 4-dimensional toroidal graph.


.. image:: /_static/square_toroidal.png
    :align: center

Wishart Planted Ensemble (WPE)
==============================







