# Candidate Research Source: VeloxQ Benchmark Instances

## Research overview

VeloxQ is a solver for quadratic unconstrained binary optimization (QUBO).
QUBO problems use binary variables taking values 0 or 1, whereas Ising
models commonly use spins taking values -1 or +1.

Pairwise QUBO problems can be converted into Ising form, making selected
benchmark instances potentially relevant to RL4Ising.

The paper evaluates VeloxQ against several quantum, classical, and
physics-inspired solvers. The preprint was first submitted in 2025 and
revised in May 2026.

## Available materials

The public repository organizes its materials into:

- `dwave-annealer/`
- `ground-state-certification/`
- `planted-solution/`
- `kipu-quantum-hubo/`

It provides small instance examples and scripts used to generate benchmark
problems. The README states that larger instances are available from the
corresponding author upon reasonable request.

The documented generation tools include the D-Wave Ocean SDK for Pegasus,
Zephyr, and Chimera structures, Chook for planted problems, and custom
Julia scripts for higher-order problems.

## Potential usefulness for RL4Ising

Selected instances could broaden the range of graph structures represented
in the dataset. Quantum-annealer connectivity differs from conventional
square grids, cubic grids, and fully connected graphs.

These problems could therefore help investigate whether an RL method
generalizes across connectivity patterns.

The planted-solution and certification materials may also offer useful
reference information, subject to verification for each selected instance.

## Full links

- Data repository: https://github.com/quantumz-io/velox-data
- Annealer benchmarks: https://github.com/quantumz-io/velox-data/tree/master/dwave-annealer
- Certification benchmarks: https://github.com/quantumz-io/velox-data/tree/master/ground-state-certification
- Planted-solution benchmarks: https://github.com/quantumz-io/velox-data/tree/master/planted-solution
- Paper: https://arxiv.org/abs/2501.19221
- Paper PDF: https://arxiv.org/pdf/2501.19221
- Preprint DOI: https://doi.org/10.48550/arXiv.2501.19221

## Reference

Pawłowski, J., Tuziemski, J., Tarasiuk, P., Louzada, H., Adamski, R.,
Hendzel, K., Pawela, Ł., & Gardas, B. (2025; revised 2026).
VeloxQ: A Fast and Efficient QUBO Solver.
*arXiv preprint*, arXiv:2501.19221.
https://doi.org/10.48550/arXiv.2501.19221

## AI Assistance Disclosure

ChatGPT (GPT-6 Astra) assisted with identifying research sources and organizing the information presented in this document.
