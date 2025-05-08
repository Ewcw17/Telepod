import qiskit
from qiskit import QuantumCircuit
from qiskit import QuantumRegister
from qiskit import ClassicalRegister
from qiskit import transpile
from qiskit_aer import AerSimulator

q1 = QuantumRegister(3)
c1 = ClassicalRegister(3)
qc = QuantumCircuit(q1, c1)

qc.x(q1[0])
qc.x(q1[1])
# qc.x(q1[2])
qc.ccx(q1[0], q1[1], q1[2])
qc.cx(q1[0], q1[1])
qc.measure(q1, c1)

aersim = AerSimulator()
compiled_circuit = transpile(qc, aersim)
result_ideal = aersim.run(compiled_circuit).result()
counts_ideal = result_ideal.get_counts()
print("counts_ideal", counts_ideal)


print(qc)

qc.draw(output='mpl', filename="circuit.png")