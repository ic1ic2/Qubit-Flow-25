## Circuit- Knitting

This notebook is a part of the IBM Quantum Challenge 2024, which uses Qiskit to explore the technique of circuit knitting. Circuit knitting refers to breaking large quantum circuits into smaller sub-circuits that can be executed independently and later classically combined to reconstruct results. The focus is on quasi-probability decomposition (QPD) for cutting distant CNOT gates into local operations.

The notebook demonstrates how multi-qubit gates—particularly those acting on non-adjacent qubits—can be replaced with QPD-based approximations using Qiskit’s `cut_gates` utility. Once decomposed, the resulting sub-experiments are compiled, transpiled, and executed individually, followed by classical post-processing of results. The impact of circuit cutting is analyzed in terms of depth reduction, with comparisons made between the depth of the full circuit and the average depth of sub-circuits. Additionally, the effect of transpilation parameters and initial qubit layout on circuit performance is examined.

Note – Some cells in the notebook may not work as expected due to the non-availability of the `qc_grader` function.