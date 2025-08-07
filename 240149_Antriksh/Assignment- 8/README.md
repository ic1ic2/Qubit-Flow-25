## Implementation of Grover's Algorithm

Grover’s Algorithm is a quantum search algorithm that identifies a target item within an unsorted database of size $N$ using only $\mathcal{O}(\sqrt{N})$ queries, providing a quadratic speedup over classical approaches.

In this implementation, 6 qubits are used, enabling exploration of a search space of size $N = 2^6 = 64$. Eight integers are selected uniformly at random between 0 and 63, each representing a distinct hidden target state $x_0$ such that $f(x_0) = 1$ and $f(x) = 0$ for all $x \neq x_0$.

For each target, an oracle operator $U_f$ is constructed to satisfy:
$$
U_f |x\rangle = (-1)^{f(x)}|x\rangle
$$
This is implemented as a diagonal gate that applies a $-1$ phase only to the target state.

The diffuser (also known as the inversion-about-the-mean operator) is constructed using:
$$
D = 2|\psi\rangle\langle\psi| - I
$$
where $|\psi\rangle$ is the uniform superposition over all basis states, prepared by applying Hadamard gates to the $|000000\rangle$ state.

Each Grover iteration consists of applying the oracle followed by the diffuser. The optimal number of iterations is:
$$
r = \left\lfloor \frac{\pi}{4} \sqrt{N} \right\rfloor = 6
$$
This sequence amplifies the amplitude of the target state.

After executing the circuit and performing measurement, the output corresponds to the most probable solution. Since each oracle circuit is executed once, the correct target state is expected to be retrieved with high probability in a single shot.

This simulation demonstrates how Grover’s algorithm can efficiently search for marked elements in a quantum system and shows the power of amplitude amplification even for randomly chosen targets.
