Quantum teleportation :-
Overview:

For the simulation of the circuit, I first considered three qubits namely q0,q1 and q2 where q0 was the qubit to be sent via the communication channel. q1 and q2 were then entangled together so as to form the entangled state of Alice and Bob. After this I had measured the value of q0 and q1 together using the reverse process of entanglement. After this the classical outputs were then passed to bob and the state of Alice collapsed. For finding bob's final state , I had then applied gates on q2 based upon the classical outputs received .

The Circuit:

For the entanglement of q1,q2  : I had applied the Hadamard gate on q1 and then used CNOT for entanglement. 
For the Alice state : I used a parametric circuit and the parameter was basically the angle by which the qubit was reported around y axis in the Bloch sphere .
For the classical measurement of Alice state and entangled state : I had first applied the CNOT on the qubits 0 and 1 and then applied Hadamard gate.
For the bob's qubit: After the measurement, Alice's state collapsed and according to the classical outputs , I applied Pauli X and Pauli Z gates or both depending upon the classical outputs .

The Result : The density matrix created in the end , was same for all measurements of classical outputs whatsoever and Bob's state matched Alice's state in all conditions which confirmed the teleportation of qubit.

Submitted by: Aaryan Pruthi  
Roll Number: 240018