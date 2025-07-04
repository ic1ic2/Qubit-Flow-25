## Implementation of the Deutsch- Jozsa Algorithm

The Deutsch- Jozsa algorithm is a quantum algorithm which determines whether a given Boolean function is constant or balanced, using just one query.

The demonstration of this algorithm involves 4 testing functions (the inputs of which are treated as decimals from $0$ to $7$)- $$f: \{0,1\}^3 \rightarrow \{0,1\}$$

- $f(x)= 0$
- $f(x)= \lfloor \frac{x}{4} \rfloor$
- $f(x)= 1$
- $f(x)= \lfloor \frac{7-x}{4} \rfloor$

Clearly, the first and the third functions are constant, while the second and the fourth are balanced. The optimal classical strategy would require $2^3 +1$ queries per function to determine its nature.

The quantum algorithm begins by initializing a quantum register of $3$ input qubits in the state $|0\rangle$ and one output qubit in the state $|1\rangle$. A Hadamard gate is then applied to all $4$ qubits, placing the input qubits in a uniform superposition over all $2^3$ possible inputs and transforming the output qubit into the state $|-\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}$. 

Now, the oracle $U_f$ is applied, performing the transformation $U_f |x\rangle|y\rangle = |x\rangle|y \oplus f(x)\rangle$ and then, a second round of Hadamard gates is then applied to the input qubits. Finally, the input register is measured. If the result is $|0\rangle^{\otimes 3}$, the function is constant; otherwise, it is balanced. 

This process allows for determination of the function’s nature with just one query, and can be generalised for any $n \in \mathbb N$, where $n$ is the number of input bits in the boolean function.