## Error- Analysis of the 2- spin and 3- Spin Heisenberg Models

### 2-Spin Heisenberg Model

For the two-qubit system, a single-step Trotter decomposition is applied to evolve the Heisenberg Hamiltonian. The initial state is set as $\left|01\right\rangle$, and the system exhibits coherent oscillations between $\left|01\right\rangle$ and $\left|10\right\rangle$, in agreement with the expected dynamics.

Fidelity between the ideal and noisy simulations remains high for small evolution times. This is due to:
- Minimal circuit depth resulting from only one Trotter step, reducing exposure to noise.
- Commuting terms in the Hamiltonian, which eliminate Suzuki-Trotter error in the evolution.

---

### 3-Spin Heisenberg Model

In the three-qubit case, a three-step Trotterization is used for simulating the evolution, in contrast to the single-step decomposition used in the corresponding model in Assignment 2. The initial state is $\left|001\right\rangle$.

Observable plots and their pairwise correlations show significant deviations when compared to the earlier implementation of the model in Assignment- 2. These discrepancies arise from:
- Increased circuit depth due to multiple Trotter steps, which amplifies the impact of noise.
- The sum of probabilities for the basis states $\left|001\right\rangle$, $\left|010\right\rangle$, and $\left|100\right\rangle$ is less than 1, despite ideally summing to unity. This indicates high noise accumulation in the circuit