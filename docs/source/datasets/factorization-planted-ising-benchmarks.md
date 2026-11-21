# Candidate Research Source: Factorization-Based Planted Ising Benchmarks

## Research overview

This study constructs benchmark problems from the multiplication of
two known prime numbers.

The arithmetic constraints are encoded as a satisfiability problem.
The known factors provide a planted solution that can be used to verify
solver output.

The paper also describes compiling the constraints into a quadratic
Ising Hamiltonian. Problem structure comes from arithmetic relationships
rather than randomly assigned spin-glass interactions.

## Available material

The author's repository includes:

- An `instances/` directory.
- Python generation scripts.
- CNF verification utilities.
- Documentation describing SAT and Ising outputs.

The README refers to Ising Hamiltonians among the intended outputs.
The completeness of that export workflow requires further inspection.

## Potential usefulness for RL4Ising

These problems could support tests of whether methods trained on random
spin glasses generalize to structured optimization problems.

Known factor pairs provide a basis for checking solutions, while factor
bit length provides a parameter for generating different problem sizes.

This source is less immediate than a collection of existing pairwise
spin-glass files.

## Full links

- Paper: https://arxiv.org/abs/2604.09837
- Paper PDF: https://arxiv.org/pdf/2604.09837
- Paper HTML: https://arxiv.org/html/2604.09837v1
- Code and instances: https://github.com/itay-hen/pq-SAT-benchmark

## Reference

Hen, I. (2026).
Planted-solution SAT and Ising benchmarks from integer factorization.
*arXiv preprint*, arXiv:2604.09837.
https://arxiv.org/abs/2604.09837

## AI Assistance Disclosure

ChatGPT assisted with identifying research sources and organizing the
information presented in this document.
