# Candidate Research Source: SWAP-Network MPS Optimization Instances

## Research overview

This study uses matrix product states (MPS) and imaginary-time evolution
to solve optimization problems.

It investigates how SWAP-network structure and variable ordering affect
the handling of interactions between variables that are far apart in
the tensor-network representation.

The experiments include synthetic graph problems and portfolio optimization.

## Available instances and supporting materials

The repository documents:

- Ten Max-Cut instances per graph family.
- Erdős–Rényi, Sherrington–Kirkpatrick, and 3-regular graph families.
- A reduced portfolio dataset with Ising/QUBO JSON files.
- Instance-generation scripts.
- Gurobi and BiqCrunch benchmark outputs.

The README's separate Zenodo DOI for simulation results was marked
"TBD" when reviewed. This should be distinguished from the benchmark
inputs already documented in the GitHub repository.

## Potential usefulness for RL4Ising

Selected instances could support comparisons between sparse and dense
interaction graphs.

The Sherrington–Kirkpatrick family is a promising starting point for
spin-glass collection. Portfolio instances could support a later
application-oriented extension.

## Full links

- Paper: https://arxiv.org/abs/2511.02980
- Paper PDF: https://arxiv.org/pdf/2511.02980
- Data and code: https://github.com/erikasgrim/swapnet-mps-ite

## Reference

Åsgrim, E. M., & Markidis, S. (2025).
SWAP-Network Routing and Spectral Qubit Ordering for MPS Imaginary-Time
Optimization.
*arXiv preprint*, arXiv:2511.02980.
https://arxiv.org/abs/2511.02980

## AI Assistance Disclosure

ChatGPT assisted with identifying research sources and organizing the
information presented in this document.
