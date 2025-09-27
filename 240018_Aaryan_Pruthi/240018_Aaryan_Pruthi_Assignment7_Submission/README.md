Implementation of the Deutsch-Jozsa Algorithm
This repository contains a Python implementation of the Deutsch-Jozsa algorithm using the Qiskit framework. The project demonstrates the algorithm's ability to determine whether a given oracle function is "constant" or "balanced" with a single query, showcasing a key example of quantum advantage over classical algorithms.

Table of Contents
Project Overview

Algorithm Details

Implementation

Results

How to Run the Code

Project Overview
The Deutsch-Jozsa problem is a foundational problem in quantum computing. It considers a function f(x) that takes an n-bit binary string as input and returns either 0 or 1. The function is guaranteed to be either:

Constant: It returns the same value (0 or 1) for all possible inputs.

Balanced: It returns 0 for exactly half of the inputs and 1 for the other half.

A classical computer would need up to 2^(n-1) + 1 queries in the worst case to solve this problem. The Deutsch-Jozsa quantum algorithm, however, can solve it with only one query to the function's quantum oracle. This project implements the algorithm for a 2-qubit input case (n=2).

Algorithm Details
The quantum circuit for the Deutsch-Jozsa algorithm is constructed as follows:

Initialize n+1 qubits to the state |0⟩.

Apply an X-gate to the last qubit to flip it to |1⟩.

Apply a Hadamard gate to all n+1 qubits.

Apply the quantum oracle corresponding to the function f(x).

Apply a Hadamard gate to the first n qubits.

Measure the first n qubits.

If the measurement result is 00...0, the function is constant. If the result is anything else, the function is balanced.

Implementation
The implementation is contained within a Jupyter Notebook (Assignment7_240018 (1).ipynb).

Framework: Qiskit and Qiskit-Aer

Simulator: The circuits are executed on the qasm_simulator.

The notebook defines:

A generic deutsch_jozsa function that constructs the circuit for a given oracle.

Two specific oracles for the n=2 case:

constant_oracle(): Implements a constant function.

balanced_oracle(): Implements a balanced function using CNOT gates.

The script then builds, transpiles, and executes the circuits for both the constant and balanced oracles, demonstrating the expected outcomes.

Results
The algorithm was executed for 1024 shots for each oracle. The measurement outcomes clearly distinguish between the two function types, as predicted by theory.

Constant Oracle: The measurement consistently yields the state 00.

Conclusion: The function is Constant.

Balanced Oracle: The measurement consistently yields the state 11.

Conclusion: The function is Balanced.

The histograms of the measurement results are saved as plot_constant.png and plot_balanced.png.

How to Run the Code
Prerequisites
Python 3.8+

Jupyter Notebook or JupyterLab

Installation
Clone the repository.

Install the necessary Python libraries. The notebook includes cells to install the dependencies directly:

pip install qiskit qiskit-aer matplotlib pylatexenc

Execution
Navigate to the repository's directory.

Start the Jupyter environment:

jupyter notebook

Open the Assignment7_240018 (1).ipynb file and run the cells sequentially.
