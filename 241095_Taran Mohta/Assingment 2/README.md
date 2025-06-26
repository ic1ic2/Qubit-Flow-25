# Assignment 2 — Digital Simulation of the 2-Spin and 3-Spin Heisenberg Model (IBM-Q)

##  Objective

This assignment involves implementing the **digital quantum simulation** of the **Heisenberg spin model** using IBM-Q's QASM simulator. The task includes:

- Constructing and simulating quantum circuits for the **2-spin** and **3-spin** Heisenberg Hamiltonians.
- Comparing the **structure**, **physical behavior**, and **computational characteristics** of both implementations.

---

##  Model: Heisenberg Hamiltonian

The **Heisenberg Hamiltonian** for a pair of spins is given by:

\[
H_{i,j} = J \left( X_i X_j + Y_i Y_j + Z_i Z_j \right)
\]

Where:
- \( J \) is the interaction strength (set to 1.0),
- \( X, Y, Z \) are Pauli matrices,
- Simulated using **RXX, RYY, RZZ** gates in Qiskit.

---

## Implementation Summary

### 2-Spin Model
- **Qubits:** 2
- **Initial state:** `|01⟩` (excitation on qubit 0)
- **Interaction:** Single pair (0–1)
- **Gates:** RXX, RYY, RZZ for evolution
- **Behavior:** Excitation oscillates between the two qubits (swap-like dynamics)

### 3-Spin Model
- **Qubits:** 3
- **Initial state:** `|010⟩` (excitation in middle qubit)
- **Interaction:** Two pairs (0–1 and 1–2)
- **Gates:** RXX, RYY, RZZ for each pair
- **Behavior:** Excitation spreads from middle qubit outward, showing transport and interference

---

## Comparison: 2-Spin vs 3-Spin

| Feature               | 2-Spin Model         | 3-Spin Model                      |
|-----------------------|----------------------|-----------------------------------|
| **Qubits**            | 2                    | 3                                 |
| **Interaction Pairs** | (0–1)                | (0–1) and (1–2)                   |
| **Initial State**     | `|01⟩`               | `|010⟩`                           |
| **Dynamics**          | Swap-like oscillation| Propagation + interference        |
| **Hilbert Size**      | \(2^2 = 4\) states   | \(2^3 = 8\) states                |
| **Gate Depth**        | Lower                | Higher                            |

Plots of the **state probabilities** over time are provided to visualize the dynamics of excitation flow.

---

## Simulation Environment

- **Simulator:** Qiskit Aer `AerSimulator()` (ideal QASM simulation)
- **Language:** Python + Qiskit
- **Tools Used:** `QuantumCircuit`, `RXX/RY/RZ gates`, `measure_all`, `matplotlib`

---

## Conclusion

This assignment demonstrates how digital quantum simulation can capture spin dynamics using only basic gates and how system complexity increases from 2 to 3 qubits.

It also lays the groundwork for **Assignment 4**, where we analyze **observables**, **fidelity**, and **error sources** under noisy simulation.
