So this is a implementation of the quantum teleportation circuit using Qiskit
the qo bit is the unknown bit which alice wants to share with bob 
Alice and Bob share q1 and q2 states which are entangled together

so first of all we take two qubits q1 and q2 make them bell states by operating the hadamard gate followed by a CNOT gate (taking q1 as control bit) , now q1 and q2 form an entangled system 
after this we apply another CNOT gate this time taking qo as the control bit  , then we do two classical measurments whose results alice shares with bob and then using these results bob finds the unknown state (qo)