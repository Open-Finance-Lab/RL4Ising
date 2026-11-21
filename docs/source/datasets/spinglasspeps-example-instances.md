# Candidate Research Source: SpinGlassPEPS.jl Example Instances

## Research overview

SpinGlassPEPS.jl is a Julia package that uses tensor networks to search
for low-energy configurations of Ising and related optimization models.

It focuses on quasi-two-dimensional graphs, which retain some grid-like
structure while allowing more complicated local connectivity.

The package approximates the Boltzmann distribution and uses that
representation to guide a search for low-energy configurations.

## Available instances and supporting materials

The repository provides:

- Example Ising inputs loaded from `examples/instances/`.
- Text-format instance files used by example scripts.
- Tools for constructing Ising graphs.
- Tools for converting groups of spins into effective Potts variables.
- Solver implementations and example workflows.

This source should be treated as a software package with example inputs,
rather than a verified large standalone dataset.

## Potential usefulness for RL4Ising

Selected instances could broaden the graph structures represented in
RL4Ising and support comparisons with a tensor-network method.

The examples may also provide manageable inputs for testing format
conversion and independent energy evaluation.

## Full links

- Published paper: https://doi.org/10.1016/j.softx.2025.102257
- arXiv: https://arxiv.org/abs/2502.02317
- Paper PDF: https://arxiv.org/pdf/2502.02317
- Repository: https://github.com/euro-hpc-pl/SpinGlassPEPS.jl

## Reference

Śmierzchalski, T., Dziubyna, A. M., Jałowiecki, K., Mzaouali, Z.,
Pawela, Ł., Gardas, B., & Rams, M. M. (2025).
SpinGlassPEPS.jl: Tensor-network package for Ising-like optimization
on quasi-two-dimensional graphs.
*SoftwareX, 31*, 102257.
https://doi.org/10.1016/j.softx.2025.102257

## AI Assistance Disclosure

ChatGPT assisted with identifying research sources and organizing the
information presented in this document.
