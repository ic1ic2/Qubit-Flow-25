In this Assignment we had implemented noise error models to both the 2-Qubit Heisenberg State Simulation as well as a 3-Qubit Heisenberg
Simulation.
***
**2-Qubit Heisenberg State**
1. Firstly we implemented the same quantum circuit as we did in Assignment 2. 
2. Then we added a 5% depolarizing error to all the gates using NoiseModel from qiskit_aer.noise.
3. Then we made a custom **fidelity function** wherein we calculated the error from ideal vs noisy simulation based on the **cosine similarity**.
4. This was to done **qasm_simulator** as the backend which gives a shot per shot distribution of probability.
5. After this we made a set of observables like **ZI**,**ZZ** wherein we tried to measure the value of the observables on the time-evolved wave-vectors.
6. After this we made a custom set of **Dynamic Correlation Functions** wherein we tried to correlate the value of one qubit on the other and its affect on time evolution.
---
**3-Qubit Heisenberg State**
1. Similar to 2 qubit heisenberg state, we made the quantum circuit as we did in Assignment 2.
2.The difference here was just of the type of observables and gates used as we scaled the model from 2-Qubit to 3-Qubit.

