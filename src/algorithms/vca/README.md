# VCA Quickstart

Environment setup: We recommend conda for the most convenient installation. Conda environment files are located at `src/envs`.

```
conda env create -f envs/vca_environment.yaml
```

Usage:

```
python vca.py [problem instance]
```

Example Ouput:

```
> python vca.py ../../dataset/EA/EA_10x10/10x10_uniform_seed1.txt

mean(E): -33.5433660848712, mean(F): -154.89824287379463, var(E): 73.85991566131288, var(F): 1.9722050905523278, #samples 50, #Training step 995
Temperature:  2
Magnetic field:  0
Elapsed time is = 136.02788472175598  seconds

Annealing step: 0.0/16
mean(E): -30.45648157385779, mean(F): -154.68102832935563, var(E): 66.25562318673148, var(F): 2.823127462608233, #samples 50, #Training step 1000
Temperature:  2.0
Magnetic field:  0.0
Elapsed time is = 136.66887617111206  seconds

Annealing step: 1.0/16
mean(E): -30.350349655435977, mean(F): -146.9989938326911, var(E): 69.15800262173676, var(F): 4.390464855014674, #samples 50, #Training step 1005
Temperature:  1.875
Magnetic field:  0.0
Elapsed time is = 137.31043696403503  seconds
```

Configuration of Wavefunction RNN and Simulated Annealing Samping procedure is located in `src/algorithms/vca/config.py`.

# Reference

This algorithm located in `src/algorithms/vca` refers to the Variational Classical Annealing algorithm in (Cheng Chen et al., 2023).

Github:

https://github.com/VectorInstitute/VariationalNeuralAnnealing

Citation: 

Fan, C., Shen, M., Nussinov, Z. et al. Searching for spin glass ground states through deep reinforcement learning. Nat Commun 14, 725 (2023). https://doi.org/10.1038/s41467-023-36363-w

Hibat-Allah, M., Inack, E.M., Wiersema, R. et al. Variational neural annealing. Nat Mach Intell 3, 952–961 (2021). https://doi.org/10.1038/s42256-021-00401-3