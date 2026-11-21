# Candidate Research Source: Heavy-Hex Ising Spin-Glass Instances

## Research overview

This study evaluates the Quantum Approximate Optimization Algorithm
(QAOA) on random-coefficient Ising models defined on heavy-hex graphs.

The experiments include systems with 16, 27, and 127 spins, together
with additional experiments at 414 qubits.

The main model family includes cubic terms: interactions involving
three spins rather than only pairs.

## Available instances and supporting materials

The LANL repository includes:

- A `problem_instances/` directory.
- Fixed heavy-hex problem instances.
- Instance-generation scripts.
- Workflows for quadratic and cubic variants.
- Code supporting related QAOA and quantum-annealing studies.

A separate Zenodo archive, `data_QAOA.tar.gz`, contains approximately
1.3 GB of data associated with the whole-chip QAOA study.

## Potential usefulness for RL4Ising

Heavy-hex instances could add another sparse connectivity pattern to
the benchmark collection.

Small quadratic instances could support loader validation and comparisons
across graph structures. Higher-order instances could support a future
extension if the project adds compatible algorithms.

## Full links

- Published paper: https://doi.org/10.1038/s41534-024-00906-w
- arXiv: https://arxiv.org/abs/2312.00997
- Paper PDF: https://arxiv.org/pdf/2312.00997
- Data and code: https://github.com/lanl/QAOA_vs_QA
- Dataset: https://zenodo.org/records/14031608
- Dataset DOI: https://doi.org/10.5281/zenodo.14031608

## Reference

Pelofske, E., Bärtschi, A., Cincio, L., Golden, J., & Eidenbenz, S. (2024).
Scaling whole-chip QAOA for higher-order Ising spin glass models on
heavy-hex graphs.
*npj Quantum Information*.
https://doi.org/10.1038/s41534-024-00906-w

## AI Assistance Disclosure

ChatGPT assisted with identifying research sources and organizing the
information presented in this document.
