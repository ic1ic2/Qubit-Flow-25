In the era of  Quantum  computers, the quantum circuits we design are rarely in a form that can be directly executed on hardware. Quantum processors have specific physical constraints, such as limited qubit connectivity and a restricted set of native gate operations.

Transpilation is the process of rewriting a given quantum circuit to be compatible with the constraints of a specific quantum device while also optimizing it to minimize errors from noise and decoherence. This project demonstrates this entire pipeline, from an abstract circuit to a hardware-compliant one.

Quantum Hardware Used: [e.g., IBM's ibmq_manila, Rigetti's Aspen-M-2, etc.]

Quantum Framework: [e.g., Qiskit, Cirq, PennyLane, etc.]

⚙️ The Six Stages of Transpilation
The transpilation process was broken down into the following six stages, with each stage's output being visualized and analyzed.

1. Circuit Decomposition
Purpose: To break down all complex or composite gates in the original circuit into the hardware's basis gate set.

In this project: The initial circuit, containing gates like Toffoli (CCX) or custom unitary gates, was decomposed into a sequence of single-qubit gates (e.g., U, RZ, SX) and two-qubit gates (e.g., CNOT) that the target hardware natively supports.

2. Initial Layout Selection
Purpose: To map the virtual qubits of the algorithm to the physical qubits on the quantum processor.

In this project: An initial mapping was chosen to best fit the circuit's two-qubit gate requirements with the hardware's qubit connectivity graph. The goal was to place qubits that interact close to each other to minimize the need for SWAP operations.

3. Routing
Purpose: To enable interactions between qubits that are not physically connected by inserting SWAP gates.

In this project: A routing algorithm was applied to the circuit. For every two-qubit gate acting on non-adjacent physical qubits, one or more SWAP gates were inserted to move the qubit states next to each other, execute the gate, and then (if necessary) swap them back.

4. Gate Optimization
Purpose: To reduce the overall gate count and circuit depth by finding and replacing redundant or inefficient gate sequences.

In this project: The circuit was scanned for patterns like consecutive identical gates that cancel out (e.g., H-H) or sequences that could be combined into a single, more efficient gate. This step is crucial for reducing the circuit's execution time and susceptibility to noise.

5. Scheduling
Purpose: To assign a precise start and end time for every operation in the circuit, respecting the hardware's timing constraints for gate execution and measurement.

In this project: An "as late as possible" scheduling algorithm was used to create the final timed sequence of operations, ensuring that no two gates were applied to the same qubit at the same time.

6. Final Compilation (Assembly)
Purpose: To convert the scheduled circuit into the low-level instruction format that the hardware's control electronics can understand.

In this project: The final scheduled circuit was converted into [e.g., QASM (Quantum Assembly Language)] code, representing the final deliverable to be sent to the quantum processor.

💻 Implementation Details
The entire pipeline was implemented using Python 3.x and the [Your Framework, e.g., Qiskit] library.

The process begins with a sample quantum circuit, such as a GHZ state or Bell state, defined in the main script (main.py or notebook.ipynb). The script then sequentially calls functions corresponding to each of the six transpilation stages, printing and visualizing the circuit's state after each transformation.
