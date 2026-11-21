# Candidate Research Source: Sidon-28 Spin-Glass Instances

## Research overview

This study investigates approximate optimization using quantum annealing
with quantum annealing correction. It evaluates Sidon-28 spin-glass
problems with mixed positive and negative interactions.

The coupling values are drawn from ±{8/28, 13/28, 19/28, 1}.
The paper studies logical problems containing 142 to 1,322 spins.

## Available instances

The University of Hamburg's `qubo-benchmark` repository documents:

- 1,386 Sidon-28 instances in the `s28-qac` family.
- 126 instances at each size level from L = 5 through L = 15.
- Compressed NumPy `.npz` input files.
- Recorded solver results and classical benchmark code.

This repository redistributes instances associated with the study.
Original source attribution should be preserved.

## Potential usefulness for RL4Ising

These instances could support experiments on how solution quality changes
with problem size and coupling precision.

Their varied interaction strengths would complement benchmarks using
only +1 and -1 couplings. They could also support time-to-target
comparisons: measuring how quickly each method reaches a specified
energy threshold.

## Full links

- Published paper: https://doi.org/10.1103/PhysRevLett.134.160601
- arXiv: https://arxiv.org/abs/2401.07184
- Paper PDF: https://arxiv.org/pdf/2401.07184
- Data repository: https://github.com/ml-uhh/qubo-benchmark

## Reference

Muñoz-Bauza, H., & Lidar, D. A. (2025).
Scaling Advantage in Approximate Optimization with Quantum Annealing.
*Physical Review Letters, 134*, 160601.
https://doi.org/10.1103/PhysRevLett.134.160601

## AI Assistance Disclosure

ChatGPT assisted with identifying research sources and organizing the
information presented in this document.
