============================================
Key Concepts
============================================

Ising Models
============================================

An Ising model consists of :math:`N` binary spins,
:math:`\sigma_i \in \{-1,+1\}`, arranged on a :math:`d`-dimensional lattice.
The couplings :math:`J_{ij}` describe interactions between spins, while
:math:`h_i` represents an external magnetic field.

The Hamiltonian gives the energy of a spin configuration. A common form is

.. math::

   H(\boldsymbol{\sigma}) = -\sum_{(i,j)} J_{ij}\sigma_i\sigma_j
   - \sum_i h_i\sigma_i.

The ground state is the spin configuration that minimizes this energy.

Boltzmann Distribution
============================================

At inverse temperature :math:`\beta`, the Boltzmann distribution assigns
higher probability to lower-energy configurations:

.. math::

   p(\boldsymbol{\sigma}) =
   \frac{e^{-\beta H(\boldsymbol{\sigma})}}{Z}.

The partition function :math:`Z` normalizes the distribution. As temperature
decreases, probability concentrates around low-energy states, connecting
statistical sampling with optimization.

Deep Reinforcement Learning
============================================

Reinforcement learning methods learn how to find low-energy spin
configurations. RL4Ising compares their results with traditional optimization
solvers.
