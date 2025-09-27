**Grover's Algorithm for Unstructured Search**
This repository provides a Python implementation of Grover's algorithm, a cornerstone of quantum computing, designed to solve **unstructured search** problems. The project demonstrates the **quadratic speedup** this quantum algorithm offers over its classical counterparts by efficiently finding a "marked" item in an unsorted database.
***
**Table of Contents**
1. Project Overview

2. Algorithm Details

3. Implementation

4. Results
***
**Project Overview**
Grover's algorithm is a quantum search algorithm that can find a unique target entry in an unsorted database of N items in approximately **O(√N)** time. Classically, this task would require O(N) time on average. This quadratic speedup makes it one of the most important quantum algorithms discovered.

This project implements Grover's algorithm to find a specific marked quantum state within a given search space. The core idea is to use a technique called amplitude amplification to iteratively increase the probability amplitude of the marked state, making it highly likely to be measured at the end of the process.
***
**Algorithm Details**
The algorithm consists of the following key steps, which are repeated for an optimal number of iterations:

**Initialization:**

Prepare a register of n qubits (where N = 2^n is the size of the search space) in an equal superposition of all possible states. This is achieved by applying a Hadamard gate to each qubit, which starts in the |0⟩ state.

This creates the state: **|s⟩ = (1/√N) Σ |x⟩ ** for all x from 0 to N-1.

**The Oracle (U_ω)**:

The oracle is a quantum black box that can recognize the solution to the search problem.

It applies a phase shift to the marked state |ω⟩. Specifically, it flips the sign of the marked state's amplitude, leaving all other states unchanged. For example: U_ω|x⟩ = -|x⟩ if x=ω, and U_ω|x⟩ = |x⟩ otherwise.

**The Amplifier / Grover Diffusion Operator (U_s)**:

This operator amplifies the amplitude of the marked state while shrinking the amplitudes of all other states.

It performs an "inversion about the mean" operation. The operator can be constructed as **U_s = H^⊗n * U_0 * H^⊗n**, where U_0 is an operator that flips the sign of the |0...0⟩ state.

These two steps (Oracle and Amplifier) are repeated approximately **(π/4)√N** times to maximize the probability of measuring the marked state.
***
**Implementation**
The implementation is contained within a Assignment_8.

Framework: Qiskit and Qiskit-Aer

Simulator: The circuit is executed on the qasm_simulator.

Target Problem: The code is configured to search for a specific n-qubit state (the "marked item"), which is defined within the oracle function.

The notebook programmatically constructs the quantum circuit, including the initialization, the custom oracle for the marked state, and the Grover diffusion operator.
***
**Results**
After the optimal number of Grover iterations, the quantum state is measured. The expected result is a high probability of measuring the marked state.

Measurement Outcome: The histogram of measurement results shows a dominant peak corresponding to the marked state, indicating the successful amplification of its probability. For example, if the marked state is |11⟩, the measurement counts for '11' will be significantly higher than for any other state ('00', '01', '10').

The results validate the theoretical quadratic speedup, as the correct state is found with high probability in a number of steps proportional to the square root of the search space size.

