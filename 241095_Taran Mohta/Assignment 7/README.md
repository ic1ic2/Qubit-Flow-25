# Deutsch–Jozsa Algorithm — Qiskit Implementation

This is the implementation of the **Deutsch–Jozsa algorithm**, one of the first quantum algorithms to demonstrate exponential speedup over classical methods.

---

## Problem Statement

Given a Boolean function:

```
f: {0, 1}^n → {0, 1}
```

with the promise that it is either:

- **Constant**: outputs 0 or 1 for all inputs
- **Balanced**: outputs 0 for half of all possible inputs and 1 for the other half

The goal is to determine whether $f$ is **constant** or **balanced**.

- **Classical approach**: requires up to $2^{n-1} + 1$ evaluations in the worst case  
- **Deutsch–Jozsa algorithm**: solves it with **1 query** using quantum computation

---

## Circuit Overview

The Deutsch–Jozsa algorithm uses $n + 1$ qubits:

- $n$ qubits for the input register, initialized to $|0\rangle^{\otimes n}$
- 1 qubit for the target, initialized to $|1\rangle$

---

### Circuit Diagram (ASCII)

```text
Deutsch–Jozsa Algorithm Circuit (n = 2 shown)

      ┌───┐              ┌───────┐      ┌────────────┐      ┌───────┐      ┌───┐
|0⟩───┤ H ├──────────────┤       ├──────┤    U_f      ├──────┤ H ⊗ n ├──────┤ M ├───
      └───┘              │       │      │             │      └───────┘      └─┬─┘
                         │       │      │             │                      │
      ┌───┐              │  n+1  │      │             │                      ▼
|0⟩───┤ H ├──────────────┤  qubit├──────┤   Oracle    ├────────────────────── M
      └───┘              │       │      │             │
                         │       │      │             │
      ┌───┐              │       │      └─────────────┘
|1⟩───┤ X ├───┤ H ├──────┘
      └───┘
```

---

## What the Algorithm Does

1. **Initialize**: the input register to $|0\rangle^{\otimes n}$ and target qubit to $|1\rangle$
2. **Apply Hadamard** gates to all qubits
3. **Apply Oracle** $U_f$:  
   $$
   U_f |x⟩|y⟩ = |x⟩|y \oplus f(x)⟩
   $$
4. **Apply Hadamard** to the first $n$ qubits again
5. **Measure** the first $n$ qubits

---

## Output Interpretation

The final histogram tells us whether $f$ is constant or balanced:

- If **only** `'000...0'` appears: $f$ is **constant**
- If **any other output** appears: $f$ is **balanced**

---
