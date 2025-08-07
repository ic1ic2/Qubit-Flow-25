## Implementation of Shor's Algorithm

Shor's Algorithm is a quantum algorithm designed to efficiently factor large composite integers. It offers an exponential speedup over classical factoring algorithms by reducing the problem to finding the order $r$ of a randomly chosen integer $a$ modulo $N$, where $N$ is the number to be factored.

The quantum portion of the algorithm relies on **Quantum Phase Estimation (QPE)** to determine the order $r$ such that:
$$
a^r \equiv 1 \ (\text{mod} \ N)
$$

### Parameter Specifications:

- **Number to be factored:** $N = 33$
- **Control register size:** 12 qubits (to achieve high precision in phase estimation)
- **Target register size:** 6 qubits (sufficient to represent numbers up to $N-1$)

A random base $a \in [2, N - 1]$ is chosen such that $\gcd(a, N) = 1$. The circuit applies Hadamard gates to the control register to create a uniform superposition, and prepares the target register in state $|1\rangle$.

Modular exponentiation is implemented implicitly, where each control qubit applies a simulated controlled-$U^{2^j}$ operation, modeled as a controlled-$X$ gate targeting the appropriate bit based on the value of $a^{2^j}\mod N$.

The **Inverse Quantum Fourier Transform (IQFT)** is applied to the control register to extract phase information corresponding to the eigenvalue of the modular exponentiation operator. This phase encodes the order $r$.

The measured outcome is processed using continued fractions to estimate $r$ from the observed phase. If $r$ is even and satisfies $a^r \mod N = 1$, then the prime factors of $N$ can be computed as:
$$
\gcd(a^{r/2} - 1, N), \quad \gcd(a^{r/2} + 1, N)
$$
This process is repeated until non- trivial factors are extracted.

This implementation iterates until valid, non-trivial factors of $N$ are obtained. The process demonstrates how quantum period finding plays a key role in efficiently factoring large integers.
