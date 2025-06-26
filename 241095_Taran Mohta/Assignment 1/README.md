# 🧠 The Quantum Teleportation Circuit

In this notebook, we implement the quantum teleportation protocol — a way to **transmit a qubit's quantum state** from one location (Alice) to another (Bob), using **entanglement and classical communication**, without physically sending the qubit itself.

---

## ⚙️ Steps in the Circuit

1. **Bell Pair Creation**  
   An entangled pair of qubits is shared between Alice (`A`) and Bob (`B`).  
   - A Hadamard gate is applied to `A`  
   - Followed by a CNOT gate from `A → B`  
   This creates a Bell state shared between Alice and Bob.

2. **Entangling the Input Qubit with the Bell Pair**  
   The qubit `Q`, which holds the state to be teleported, is entangled with Alice's part of the Bell pair.  
   - A CNOT gate is applied from `Q → A`  
   - Then a Hadamard gate is applied on `Q`

3. **Measurement by Alice**  
   Alice measures both her qubits (`Q` and `A`) in the standard basis.  
   - The measurement results are stored in classical bits `q` and `a`.

4. **Classical Communication & Bob’s Correction**  
   Alice sends the classical bits `q` and `a` to Bob.  
   Bob applies conditional operations based on these bits:  
   - If `a = 1`, apply an **X gate** to `B`  
   - If `q = 1`, apply a **Z gate** to `B`

---

## ✅ Result

After applying these corrections, **Bob’s qubit `B` contains the same quantum state that was originally held by `Q`**, completing the teleportation.

This protocol is a foundational example of how quantum entanglement and classical information together enable novel quantum communication tasks.
