# Reinforcement Learning for Ising Problem Documentation

## Structure

The documentation is organized as follows:

- **Home**: Homepage with links to documentation
- **[User Documentation](source/user/)**: Overview of project, usage, and motivation beind our work.

Each folder contains either .rst or .nblink files that can be modified to change the content on the site.

Alternatively, you can clone this repository and build the documentation locally, using conda:

```bash
# Clone the repository
git clone https://github.com/YangletLiu/RL4Ising.git

# Navigate to the docs folder
cd RL4Ising/docs

# Install dependencies
conda env create --name test --file environment.yml

# Activate environment  
conda activate test

# Build the documentation
sphinx-build -b html source/ _build/
```

The output HTML files will be located in the `_build/` directory.