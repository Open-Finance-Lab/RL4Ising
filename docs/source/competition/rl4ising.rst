================
Task 2: RL4Ising
================

RL4Ising is a task that challenges you to build agents that find ground state solutions to Ising models. Your mission: train agents that can effectively navigate the huge discrete space of the Ising model to find the groud-state solution.

Task Overview
-------------
In this task, participants are invited to develop agents that explore the solution space of the Ising model and find high quality solutions. 

Why this Matters
----------------
Modern RL models fall victim to the huge solution space and optimization plateau. They tend to have trouble efficiently exploring the discrete space and improving the quality of their solutions.

RL4Ising introduces a curriculum learning solution with:

- Masked Transformers: Learn an attend to increasing sized portions of the Ising model.

Data
----