# Candidate Research Source: Posiform-Planted QUBO Instances

## Research overview

Posiform planting constructs quadratic unconstrained binary optimization
(QUBO) problems with a unique known optimal solution.

The method allows different connectivity patterns, including Chimera,
Pegasus, and Zephyr graphs. It also includes linear terms, which must
be handled correctly when converting the problems into Ising form.

## Available data

The authors provide a Zenodo dataset associated with the paper:

- Archive filename: `dataset_export.tar.gz`.
- Approximate archive size: 835 MB.
- Dataset DOI: 10.5281/zenodo.8336707.

The archive's internal file formats and instance-level metadata should
be inspected before selecting files for RL4Ising.

## Potential usefulness for RL4Ising

Known optimal solutions would allow direct measurement of energy error
and the fraction of runs that recover the optimum.

The different connectivity patterns could also support comparisons
across graph structures and tests of generalization.

## Full links

- Published paper: https://doi.org/10.3389/fcomp.2023.1275948
- arXiv: https://arxiv.org/abs/2308.05859
- Paper PDF: https://arxiv.org/pdf/2308.05859
- Dataset: https://zenodo.org/records/8336707
- Dataset DOI: https://doi.org/10.5281/zenodo.8336707

## Reference

Hahn, G., Pelofske, E., & Djidjev, H. N. (2023).
Posiform planting: generating QUBO instances for benchmarking.
*Frontiers in Computer Science, 5*, 1275948.
https://doi.org/10.3389/fcomp.2023.1275948

## AI Assistance Disclosure

ChatGPT assisted with identifying research sources and organizing the
information presented in this document.
