SPIN HEISENBERG MODELS : Basically these models try to simulate a 2 spin or a n spin state model . The main objective of this model is to simulate the time variance of a wavefunction.

1.2 spin Heisenberg model : In this model the Hamiltonian is H = J/4(X1X2 + Y1Y2 + Z1Z2) where X,Y,Z are the pauli gates . Now here we apply these gates and then use the important relation of a time dependent Schrodinger's Equation which is let |X> be any wavefunction then |X> * e^(-iEt) ,where E = H|X>, give the state vector at an arbitrary time t.
So using this I modeled my circuit and then applied it on the IBM Brisbane Quantum Computer. Note I didn't use |00> state as my input state as it is already an eigenvector of the H operator so I used |01> state as my initial state where '0' in |01> is qubit 1 and '1' in |01> is qubit 0 following the big-endian system in Qiskit.

2. 3 spin Heisenberg model : Not much is different apart from the fact that the Hamiltonian is now changed to J/4(X1X2 + Y1Y2+Z1Z2+X2X3+Y2Y3+Z2Z3) and then rest is same.


Results:1. In the first model I found that the probability of |01> and |10> states were fluctuating but the 00 and 11 state were practically 0. 
2. In the second model the probability for |001> and |100> were fluctuating but that for |010> was very less and attains it maximum of 0.2 and the rest probabilities of bits strings were 0.
