# Assignment 4: Observables, Fidelity, and Error Analysis in Digital Quantum Simulations

This assignment builds upon the Heisenberg model simulations implemented in Assignment 2. It investigates how observable quantities evolve over time in both 2-spin and 3-spin systems, and evaluates the effect of quantum noise on simulation accuracy using fidelity as a metric. The simulations were run using the QASM simulator, with and without noise.

---

## Overview

1. Simulation of Heisenberg time evolution (2-spin and 3-spin models)  
2. Computation of expectation values and dynamical correlation functions  
3. Simulation with realistic noise using `FakeSherbrooke`  
4. Fidelity analysis between noisy and ideal simulations  
5. Discussion of errors: Suzuki–Trotter decomposition and hardware noise

---

## 1. Model Setup

The Heisenberg Hamiltonian for two and three spins is implemented using parameterized gates:

- `rxx`, `ryy`, and `rzz` simulate the X, Y, and Z coupling terms.
- The initial states are prepared as anti-aligned for 2-spin (`|01⟩`) and central excitation for 3-spin (`|010⟩`).
- Evolution is simulated for time values `t ∈ [0, 6π]`.

---

## 2. Observables Computed

We extract the following expectation values from QASM output:

- ⟨Z₀⟩, ⟨Z₁⟩, ⟨Z₂⟩: Spin direction on each qubit  
- ⟨ZᵢZⱼ⟩: Correlations between qubit pairs  
- Corrᵢⱼ = ⟨Zᵢ⟩ − ⟨Zⱼ⟩

These reveal how the spin excitation propagates and interferes across the system over time.

---

## 3. Noisy Simulation and Fidelity

To model realistic quantum execution, we simulate the circuits with noise using the `FakeSherbrooke` backend. Fidelity is used to quantify the accuracy of the noisy output relative to the ideal result.

### Fidelity Computation

Fidelity is approximated using the Bhattacharyya coefficient between the two distributions:

Fidelity ≈ (1 / N) × ∑ₖ √(P_ideal(k) × P_noisy(k))

Where `P(k)` are the observed probabilities of output state `k`.

---

## 4. Results and Analysis

### Observables (QASM Simulation without Noise)

- In the **2-spin model**, ⟨Z₀⟩ and ⟨Z₁⟩ oscillate sinusoidally in opposite phase, consistent with excitation swap.
- The **3-spin system** shows more complex patterns, with energy spreading from the center qubit outward, leading to interference effects.

### Fidelity vs Time (QASM with Noise)

| Metric                    | 2-Spin Model | 3-Spin Model |
|---------------------------|--------------|--------------|
| Max Fidelity              | ~0.985       | ~0.973       |
| Min Fidelity              | ~0.976       | ~0.952       |
| Trend                     | Smooth decay | Noisy decay  |
| Stability                 | High         | Fluctuating  |

The 3-spin simulation experiences faster and more irregular fidelity degradation due to higher gate count, deeper circuits, and a larger Hilbert space.

---

## 5. Error Sources

### Suzuki–Trotter Error

- The time evolution operator is approximated by splitting exponentials of non-commuting Hamiltonian terms.
- This error increases with larger time steps.
- Repeating shorter layers (Trotterization) can reduce this error.

### Hardware Noise

- Modeled using the fake backend which includes:
  - Gate infidelity
  - Qubit decoherence
  - Readout error
- Noise impact accumulates with circuit depth and qubit count.

### Error Comparison

| Error Type           | 2-Spin Severity | 3-Spin Severity |
|----------------------|-----------------|------------------|
| Trotter Error        | Moderate        | High             |
| Gate Noise           | Low             | Higher           |
| Readout Noise        | Low             | Higher           |

At small time values, simulation error is dominated by approximation (Trotter error). At large times, noise becomes the dominant source of fidelity loss.

---

## Conclusion

The simulation and analysis show that as system size increases, both Trotter approximation and hardware noise have a more pronounced effect. The 3-spin model clearly exhibits stronger sensitivity to noise and depth, reinforcing the importance of error mitigation and smarter circuit design in practical quantum simulations.
