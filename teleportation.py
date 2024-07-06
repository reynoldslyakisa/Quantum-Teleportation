from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a Quantum Circuit with 3 qubits and 3 classical bits
qc = QuantumCircuit(3, 3)

# Prepare an entangled state
qc.h(1)
qc.cx(1, 2)

# Add a barrier
qc.barrier()

# Apply teleportation protocol
qc.cx(0, 1)
qc.h(0)
qc.barrier()
qc.measure([0, 1], [0, 1])
qc.cx(1, 2)
qc.cz(0, 2)
qc.measure(2, 2)

# Execute the circuit
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
qobj = assemble(compiled_circuit)
result = simulator.run(qobj).result()

# Get the result and plot the histogram
counts = result.get_counts(qc)
plot_histogram(counts)
plt.savefig('results/teleportation_results.png')
plt.show()
