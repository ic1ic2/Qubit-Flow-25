
import matplotlib.pyplot as plt
import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit_aer import AerSimulator


classic = ClassicalRegister(2, 'c')  
quant = QuantumRegister(3, 'q')

circuit = QuantumCircuit(quant, classic) 


circuit.h(quant[0])    #hadamard gate on q0
circuit.barrier()

circuit.h(quant[1])         #entagle q1 and q2
circuit.cx(quant[1], quant[2])

circuit.cx(quant[0], quant[1])      #entangle q0 and q1
circuit.h(quant[0])
circuit.barrier()

circuit.measure(quant[0], classic[0])     #measuring qubits and then saving as classical bits
circuit.measure(quant[1], classic[1])


if classic[0] == 0 and classic[1] ==1:        #measuring q0 and q1 and then applying gates accordingly
    circuit.x(2)            


elif classic[0] == 1 and classic[1] ==0:
    circuit.z(2)           


elif classic[0] == 1 and classic[1] ==1:
    circuit.x(2)
    circuit.z(2)        



circuit.draw('mpl')        #drawing the plot
#circuit.barrier is used to add the barrier between two operation

sim = AerSimulator()
job = sim.run(circuit)
result = job.result()
counts = result.get_counts()
plot_histogram(counts)