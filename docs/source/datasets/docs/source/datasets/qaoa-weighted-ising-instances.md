# Candidate Research Source: Weighted Ising Instances for QAOA

## Research overview

This paper studies parameter selection for the Quantum Approximate
Optimization Algorithm (QAOA), focusing on its single-layer version.

The research evaluates weighted Ising problems, including experiments
with 128 and 256 variables. The preprint first appeared in 2025, and
the published article appeared in 2026.

## Available instances

The authors' repository includes:

- A `benchmark_data/` directory containing generated graph instances.
- Instances with and without external magnetic fields.
- Gurobi's best-found solutions and corresponding MIP gaps.
- Implementations of QAOA, recursive QAOA, and comparison methods.
- Numerical results and plotting utilities.

A MIP gap indicates the remaining difference between a solver's
incumbent solution and its bound. A best-found solution should not
automatically be described as a proven optimum.

## Potential usefulness for RL4Ising

These instances could provide weighted problems with reference solver
information, helping the team evaluate solution quality more carefully.

The instances without external fields are a practical starting point
for assessing compatibility with RL4Ising's existing input format.

## Full links

- Published paper: https://doi.org/10.22331/q-2026-07-15-2158
- arXiv: https://arxiv.org/abs/2501.16419
- Paper PDF: https://arxiv.org/pdf/2501.16419
- Data and code: https://github.com/vijeycreative/NOpt_QAOA1_Tuning

## Reference

Vijendran, V., Koh, D. E., Bae, E., Kwon, H., Lam, P. K., & Assad, S. M.
(2026). Near-Optimal Parameter Tuning of Level-1 QAOA for Ising Models.
*Quantum, 10*, 2158.
https://doi.org/10.22331/q-2026-07-15-2158

## AI Assistance Disclosure

ChatGPT assisted with identifying research sources and organizing the
information presented in this document.
