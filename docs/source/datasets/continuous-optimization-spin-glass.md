# Candidate Research Source: Continuous Optimization for the Spin Glass Problem

## Research overview

This paper studies a continuous formulation of the spin-glass ground-state
problem. Instead of restricting every variable immediately to -1 or +1,
the formulation allows variables to range over the interval [-1, 1].

The authors explain why the continuous and discrete formulations have the
same global minimum for the pairwise model considered, and how a continuous
global minimizer can be converted into a discrete spin configuration.

The formulation remains nonconvex. It does not make general spin-glass
optimization easy or guarantee that an arbitrary local minimum is a ground
state.

## Available benchmark sources

The accessible preprint identifies:

- The `rudy` and `ising` classes from the Biq Mac library.
- Selected larger instances from the Gset collection.
- An authors' GitHub repository containing experimental code and
  parameter files.

The reported Biq Mac experiments include `rudy` instances with 60, 80,
and 100 variables, and `ising` instances with 100, 150, 250, and
300 variables.

These are established benchmark sources reused by the study, rather than
necessarily new datasets introduced by the paper.

## Potential usefulness for RL4Ising

This source could help the team connect RL experiments with established
mathematical optimization benchmarks.

It also offers a possible additional classical formulation to investigate.
Comparing different formulations on identical instances could reveal whether
a performance difference comes from the search method or the problem encoding.

The benchmark collections provide an opportunity to document source instance
identifiers and reference objectives more systematically.

## Full links

- Paper: https://arxiv.org/abs/2512.05852
- Paper PDF: https://arxiv.org/pdf/2512.05852
- Accessible paper text: https://arxiv.org/html/2512.05852v1
- Published article DOI: https://doi.org/10.1016/j.physa.2026.131356
- Authors' repository: https://github.com/luizleduino/spinglassmodel
- Biq Mac library: https://biqmac.aau.at/biqmaclib.html
- Gset collection: http://web.stanford.edu/~yyye/yyye/Gset/

## Reference

Duxbury, P., Lavor, C., & de Salles-Neto, L. L. (2026).
A continuous nonlinear optimization perspective on the Spin Glass Problem.
*Physica A: Statistical Mechanics and its Applications, 686*, 131356.
https://doi.org/10.1016/j.physa.2026.131356

A preprint was submitted in December 2025:
https://doi.org/10.48550/arXiv.2512.05852

## AI Assistance Disclosure

ChatGPT (GPT-6 Astra) assisted with identifying research sources and organizing the information presented in this document.
