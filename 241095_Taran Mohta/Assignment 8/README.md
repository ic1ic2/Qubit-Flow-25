# Grover's Algorithm — Qiskit Implementation

This assignment implements **Grover's quantum search algorithm**. The algorithm finds a marked item $x^*$ from an unstructured list of size $N = 2^n$ with high probability using $\mathcal{O}(\sqrt{N})$ queries.

---

## Problem Statement

Given a Boolean function:

```
f: {0, 1}^n → {0, 1}
```

such that:

- $f(x) = 1$ for exactly one unknown $x = x^*$
- $f(x) = 0$ for all $x 
e x^*$

The goal is to find $x^*$ using as few queries as possible.

---

## Classical vs Quantum

- **Classical search**: $\mathcal{O}(2^n)$ queries  
- **Grover’s algorithm**: $\mathcal{O}(\sqrt{2^n})$ queries

---

## Algorithm Overview

1. Initialize $n$ qubits in the $|0\rangle^{\otimes n}$ state.
2. Apply Hadamard gates to create uniform superposition.
3. Repeat the **Grover operator** $R$ times:
   - **Oracle** $U_f$: flips the phase of $|x^*\rangle$
   - **Diffusion operator** $D$: reflection about the average
4. Measure in the computational basis.

Optimal number of iterations:

```
R ≈ ⌊(π / 4) * √N⌋
```

---

## Circuit Structure (ASCII Diagram)

```text
Grover's Algorithm Circuit (n = 3)

      ┌───┐                     ┌────────┐     ┌────────────┐     ┌────────┐     ┌───┐
|0⟩───┤ H ├──■────── Uf ───────┤        ├─────┤  Diffusion ├─────┤        ├─────┤ M ├───
      └───┘  │                 │        │     └────────────┘     │        │     └─┬─┘
             │   repeat R times│  Oracle│                       Hadamards │       ▼
|0⟩───┤ H ├──■─────────────────┤        ├────────────────────────┤        ├─────── M
```

---

## Output Interpretation

After simulation, the result with the **highest probability** corresponds to the **marked item** $x^*$. The probability increases quadratically with each Grover iteration.

---
