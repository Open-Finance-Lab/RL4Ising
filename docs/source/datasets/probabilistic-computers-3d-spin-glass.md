# Candidate Research Source: 3D Spin Glasses for Probabilistic Computing

## Research overview

This study investigates classical approaches to difficult three-dimensional
spin-glass optimization problems. It evaluates adaptive parallel tempering
(APT) and discrete-time simulated quantum annealing (DT-SQA), comparing
their performance with a quantum annealer on the same problem instances.

Parallel tempering explores a problem using multiple replicas at different
temperatures. Exchanges between replicas can help the search escape local
minima. The study also considers isoenergetic cluster moves, which make
collective changes to groups of spins.

Its relevance to RL4Ising comes from the shared problem instances and
classical comparison methods, regardless of the hardware focus of the paper.

## Available instances and supporting materials

The companion repository includes:

- `logicalMatInstances/`: logical problem instances.
- `matInstances/size15/`: embedded instances.
- `putativeGroundEnergies/`: candidate ground-state reference energies.
- `APT.m` and `SQA.m`: MATLAB solver implementations.
- Annealing schedules and processed experimental results.

The README documents logical size settings of 8, 10, 12, 15, and 16,
and instance IDs from 0 through 299. It also documents an embedded size
setting of 15.

The instances are provided through MATLAB files. The README describes
50 independent experiments per instance as the setting used in the work.

## Potential usefulness for RL4Ising

This source could support experiments on how solution quality and runtime
change as three-dimensional problems become larger.

The accompanying APT and SQA implementations offer potential classical
baselines for evaluating RL methods on matching inputs. The schedules and
reference-energy files could also help document reproducible comparisons.

Logical instances are the most direct starting point for collection.
Embedded instances should be cataloged separately because embedding changes
the graph representation and can introduce additional physical variables.

## Full links

- Repository: https://github.com/OPUSLab/3DSpinGlassWithPbits
- Logical instances: https://github.com/OPUSLab/3DSpinGlassWithPbits/tree/main/logicalMatInstances
- Reference energies: https://github.com/OPUSLab/3DSpinGlassWithPbits/tree/main/putativeGroundEnergies
- APT implementation: https://github.com/OPUSLab/3DSpinGlassWithPbits/blob/main/APT.m
- SQA implementation: https://github.com/OPUSLab/3DSpinGlassWithPbits/blob/main/SQA.m
- Paper: https://arxiv.org/abs/2503.10302
- Paper PDF: https://arxiv.org/pdf/2503.10302
- Published article DOI: https://doi.org/10.1038/s41467-025-64235-y

## Reference

Chowdhury, S., Aadit, N. A., Grimaldi, A., Raimondo, E., Raut, A.,
Lott, P. A., Mentink, J. H., Rams, M. M., Ricci-Tersenghi, F.,
Chiappini, M., Theogarajan, L. S., Srimani, T., Finocchio, G.,
Mohseni, M., & Camsari, K. Y. (2025).
Pushing the boundary of quantum advantage in hard combinatorial
optimization with probabilistic computers.
*Nature Communications, 16*, 9193.
https://doi.org/10.1038/s41467-025-64235-y

## AI Assistance Disclosure

ChatGPT (GPT-6 Astra) assisted with identifying research sources and organizing the information presented in this document.
