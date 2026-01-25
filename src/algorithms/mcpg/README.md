# MCPG Quickstart
Environment setup: We recommend conda for the most convenient installation.

```
conda env create -f envs/mcpg_environment.yaml
```

Usage:

```
python mcpg.py ising_default.yaml [problem instance]
```

Example Ouput:

```
> python mcpg.py ising_default.yaml ../../dataset/EA/EA_10x10/10x10_uniform_seed1.txt

o -78.650
o -78.650
o -78.650
o -78.650
o -78.650
o -78.650
OUTPUT: -78.650406
DATA LOADING TIME: 4.3900
MCPG RUNNING TIME: 14.1647
```

Configuration of Local Search and Sampling frequency is located in `src/algorithms/mcpg/ising_default.yaml`.

# Reference

This algorithm located in `src/algorithms/mcpg` refers to the MCPG algorithm in (Cheng Chen et al., 2023).

Github:

https://github.com/optsuite/MCPG

Citation: 

Chen, Cheng & Chen, Ruitao & Li, Tianyou & Ao, Ruicheng & Wen, Zaiwen. (2025). A Monte Carlo Policy Gradient Method with Local Search for Binary Optimization. Mathematical Programming. 10.1007/s10107-025-02277-2. https://arxiv.org/abs/2307.00783