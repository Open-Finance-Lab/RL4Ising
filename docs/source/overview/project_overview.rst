================
Overview
================

.. contents:: Table of Contents
   :local:

Introduction
===============================
Welcome to `Reinforcement Learning for Ising Model <https://github.com/YangletLiu/RL4Ising>`_! 

This project showcases a variety of approaches designed to find the ground state of Ising models. While our methodology focuses on the application of reinforcement learning (RL), we provide
a range of alternative methods that can be used for benchmarking and evaluation. The goal is to explore innovative RL techniques to improve the efficiency and accuracy of Ising model solutions
while providing a comprehensive dataset to compare and reproduce results.

Our Project offers:

- **Comprehensive Dataset**: Detailed collection of synthetic and real Ising model instances
- **Tutorials**: Step-by-step analysis and code for various SOTA Ising model solvers
- **Benchmarks**: Evaulate performance of various SOTA Ising model solvers

.. This repository includes a series of notebooks with code to execute and evaluate a transformer-based algorithm for solving the Ising model. A notable feature of our implementation is the
.. use of **curriculum learning**, which is designed to progressively enhance the performance of our model, leading to more efficient and accurate solutions. 

Motivation
==========

The Ising model has been a fundamental problem in statistical physics for over a century, providing insight into phase transitions, magnetism, and critical phenomena. Our objective is to
leverage the advances in RL to offer a more effective approach to finding solutions of the Ising model.

Through this project, we systematically demonstrate the advantages of different model architectures and learning paradigms when applied to the Ising model. By doing so, we strive to
showcase the strength of RL applied to this problem.

Chiefly, our goal is to illustrate that RL approaches can surpass traditional methods in both performance and scalability. Moreover, we believe RL-based methods have the potential to
advance what has been a long-standing challenge in physics and related fields.


Significance of Ising Model
---------------------------

The Ising model, a mathematical model in statistical mechanics, has been a cornerstone in modeling a variety of physics-based systems. The model involves a lattice of spins, each of which
are in one of two states, with interactions dependent on neighboring spins. Finding solutions to the Ising model is critical in effectively simulating and understanding physical
phenomena. Further, the Ising model problem can be abstracted to various other fields, such as computer science, social science, and biology. Developing an efficient solver to this problem 
would enable advancements in fields broader than solely physics.

Traditionally, the Ising model has been approached with techniques like Monte Carlo simulation. While this method provides high-quality results, it can be computationally expensive,
especially in high-dimensional systems. Moreover, obtaining high-quality solutions in complex systems is difficult due to the nonconvex, large solution space. Recently, reinforcement 
learning paradigms have been able to efficiently learn NP-hard problems such as the Ising model, and can find high-quality solutions. 


Introduction to Reinforcement Learning
--------------------------------------

Reinforcement Learning is a type of machine learning where an agent learns to make decisions by interacting with an environment and receiving feedback in the form of rewards and penalties.
Through repetitive trials, the agent learns to perform actions that maximize a long-term reward. This type of feedback system can be applied to the Ising model where rewards can be given
as the agent arranges the spins more closely to a ground state configuration.


Why Reinforcement Learning
--------------------------

...

RL Applications Towards Ising Model Solutions
-----------------------------------------------

We will now highlight some of the benefits of RL, and how they apply to the Ising model.

1) **Efficient Exploration of Solution space:** One of the largest constraints when solving the Ising model is the vast number of configurations. Traditional methods may use techniques
   such as random sampling to find potential solutions to the problem. This becomes extremely inefficient for large systems and encourages the use of alternative solvers that employ
   stochastic methods of finding solutions. RL, however, can guide the exploration of the spin configurations more effectively. By training an agent to explore the solution space, it
   can learn the most promising regions of the graph to focus on, thus speeding up convergence to high-quality solutions.
2) **Improving Quality of Solutions:** By using RL to optimize the configurations of spins, the agent can minimize the energy of a system more efficiently than traditional methods. This
   translates to solutions being found that are closer to the optimal solution. This improvement is beneficial in large systems or systems with complex interactions.
3) **Real-time Adaptation:** Another advantage of RL is its ability to adapt in real-time. In the context of the Ising model, this mean that the RL agent can adjust its strategy as it explores the environment.

The integration of RL as a solver for the Ising model holds great promise for improving efficiency and accuracy. In particular, by leveraging RL's capabilities for dynamic adaptation,
efficient exploration, and quality optimization, an RL-enabled solver can outperform traditional methods.



Goals
=====

Dataset
-------

...

Benchmark
---------

...

Tutorials
----------

...

The primary goal of this project is to create a comprehensive dataset and benchmark for solving the Ising model. This dataset will serve as a resource for researchers and developers aiming
to compare and evaluate a range of solvers and methodologies on the Ising model. By providing a consistent, reproducible framework, the project seeks to facilitate comparisons for the
development of new techniques.

1) **Constructing a Robust Dataset:** The dataset will consist of a variety of Ising model configurations across different system sizes, lattice types, and Ising model types. These diverse
   datasets will enable the testing of solvers spanning real-world scenarios. This ensures that each method can be evaluated on instances that range from easy to hard to fully capture
   the solver's ability. By including various boundary conditions, spin interactions, and lattice structures, the dataset will ensure that all important aspects of the Ising model are
   represented.
2) **Benchmarking Solvers:** A key objective is to establish benchmarks for comparing the performance of different solvers for the Ising model. These benchmarks will provide information
   on both the efficiency and quality of the solver. We will compare the strengths and weaknesses of each solver across different conditions and help researchers identify the best methods. 
3) **Reproducibility:** To encourage the continued evolution of solvers for this problem, all data and experiments will be made publicly available, allowing other researchers to reproduce
   the findings. This reproducibility is crucial for validating new methods and ensuring advances made are based on verifiable results. By providing detailed codebases, this project aims
   to contribute to the broader scientific community and accelerate the pace of research in statistical mechanics, machine learning, and optimization.