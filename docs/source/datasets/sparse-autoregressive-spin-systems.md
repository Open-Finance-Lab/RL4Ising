# Candidate Research Source: Sparse Autoregressive Neural Networks for Classical Spin Systems

## Collection status

Candidate source for external spin-glass data collection.
Instance conversion, validation, and comparison with the existing RL4Ising
dataset remain to be completed.

## Research overview

This paper introduces TwoBo, an autoregressive neural network designed for
systems with pairwise spin interactions. An autoregressive model generates
a spin configuration sequentially, using previously generated spins to
determine the probability of subsequent spins.

TwoBo incorporates information about the physical interactions into its
architecture. The study evaluates its ability to approximate Boltzmann
distributions and sample low-energy configurations on disordered systems.

The research is relevant to RL4Ising because it provides concrete problems
used to evaluate a learning-based approach to classical spin systems.
However, its principal task is distribution approximation, so its reported
metrics should not automatically be treated as ground-state benchmark results.

## Available instances

The study considers:

- Two-dimensional Edwards–Anderson spin glasses.
- Three-dimensional Edwards–Anderson spin glasses.
- Random regular graphs with degree 3: each spin has three neighbors.

The experiments use randomly assigned couplings of +1 or -1 and zero
external fields. The grid models use periodic boundary conditions.

The repository contains an `instances/` directory and a generator,
`create_instances.py`. The generator saves sparse coupling matrices as
SciPy `.npz` files, retaining only the upper triangular part.

For random regular graphs, the generator specifies 32, 64, 128, 256,
512, and 1,024 spins.

## Potential usefulness for RL4Ising

These instances could support comparisons across different graph structures.
Two-dimensional grids, three-dimensional grids, and random regular graphs
have different connectivity patterns, allowing the team to investigate
whether a method's performance depends on geometry.

The mixed-sign couplings make this a relevant source for the team's
spin-glass collection work. Existing files also provide a practical starting
point without requiring new instance generation.

## Collection and integration considerations

1. Begin with the committed instance files. The generator warns that changes
   in NetworkX edge ordering may prevent exact reproduction of those files.
2. Load the files as SciPy sparse matrices and preserve each interaction once.
3. Verify spin count, coupling signs, boundary conditions, and energy convention.
4. Record the original filename, source URL, and repository commit.
5. Check whether reference energies are available for individual files and
   distinguish proven optima from best-known values.
6. Compare the selected instances against RL4Ising before importing them.

The repository identifies an Apache-2.0 license; retain the relevant
license and attribution information when reusing its materials.

## Full links

- Repository: https://github.com/cqsl/sparse-twobody-arnn
- Instance directory: https://github.com/cqsl/sparse-twobody-arnn/tree/master/instances
- Generator: https://github.com/cqsl/sparse-twobody-arnn/blob/master/create_instances.py
- Paper: https://arxiv.org/abs/2402.16579
- Paper PDF: https://arxiv.org/pdf/2402.16579
- Published article DOI: https://doi.org/10.1088/2632-2153/ad5783

## Reference

Biazzo, I., Wu, D., & Carleo, G. (2024).
Sparse autoregressive neural networks for classical spin systems.
*Machine Learning: Science and Technology, 5*, 025074.
https://doi.org/10.1088/2632-2153/ad5783

## AI Assistance Disclosure

ChatGPT (GPT-6 Astra) assisted with identifying research sources and organizing the information presented in this document.
