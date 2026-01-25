## ⚠️ Environment Notes (VNA Reproduction)

This project reproduces **Variational Neural Annealing (VNA)** using the **original legacy implementation**.  
To ensure faithful reproduction and fair benchmarking, we intentionally preserve the original software stack.

### Software Stack
- **Python:** 3.7  
- **TensorFlow:** 1.13 (TensorFlow 1.x)
- **Purpose:** Reproducing original VNA results and running benchmarks (not framework modernization)

> **Important:**  
> Please **do NOT upgrade Python or TensorFlow** in this environment.  
> The legacy setup is required for compatibility with the original VNA codebase.

---



## Environment Support

We provide Jupyter Notebooks to allow students and users to **run VNA benchmarks interactively** under the same experimental setup.

### VCA Quickstart
Environment setup: We recommend conda for the most convenient installation.

```
conda env create -f VNAtutorial.yml
```

If you have not registered the kernel yet, run:
```
conda install ipykernel
python -m ipykernel install --user \
  --name rl4ising \
  --display-name "Python (rl4ising)"
```
You only need to do this once per machine.

After creating the environment, activate it:
```
conda activate vca
```

Inside Jupyter Notebook:
Kernel → Change Kernel → Python (vca, TF1.13)

Then follow the instructions of the Jupyter Notebook.
