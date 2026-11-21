# Candidate Research Source: Chook Planted-Solution Generator

## Research overview

Chook is an open-source Python tool for generating binary optimization
problems with planted solutions.

A planted solution is a known optimum incorporated into the construction
of an instance. This gives researchers a reference for measuring solution
quality without first solving every generated problem from scratch.

Knowing the optimum does not necessarily make finding it computationally
easy for a solver. The paper describes problem families with tunable
complexity and different graph structures.

## Supported problem families and outputs

The documented families include:

- Tile planting on two-dimensional and three-dimensional structures.
- Wishart planting.
- Deceptive cluster loops.
- Equation planting using k-regular k-XORSAT.
- k-local planting, including higher-order problems.

The tool supports text and JSON output. Its documentation states that
ground-state energies are written separately to `gs_energies.txt`.
For XORSAT problems, the file also records ground-state degeneracies.

The repository identifies an Apache-2.0 software license.

## Potential usefulness for RL4Ising

Chook could support controlled experiments where the team varies problem
size, structure, or generation parameters while retaining a known optimum.

For minimization, the quantity

`energy_error = returned_energy - ground_state_energy`

provides a direct measure of solution quality when both energies use the
same convention. The team could also measure the fraction of repeated
runs that reach the known optimum.

These properties make planted instances useful for checking energy
evaluators, evaluating search reliability, and constructing reproducible
benchmark families.

## Full links

- Repository: https://github.com/dilinanp/chook
- Documentation: https://github.com/dilinanp/chook/blob/master/README.md
- Example configuration: https://github.com/dilinanp/chook/blob/master/params.in
- Paper: https://arxiv.org/abs/2005.14344
- Paper PDF: https://arxiv.org/pdf/2005.14344
- Preprint DOI: https://doi.org/10.48550/arXiv.2005.14344

## Reference

Perera, D., Akpabio, I., Hamze, F., Mandrà, S., Rose, N.,
Aramon, M., & Katzgraber, H. G. (2020; revised 2021).
Chook—A comprehensive suite for generating binary optimization problems
with planted solutions.
*arXiv preprint*, arXiv:2005.14344.
https://doi.org/10.48550/arXiv.2005.14344

## AI Assistance Disclosure

ChatGPT (GPT-6 Astra) assisted with identifying research sources and organizing the information presented in this document.
