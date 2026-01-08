from circuit.nodes.Node import Node
from circuit.CircuitSolver import CircuitSolver

from circuit.components.Resistance import Resistance
from circuit.components.Source import Source
from circuit.components.Diode import Diode

# Constant rotation
omega = 50

# Create nodes
node1 = Node()
node2 = Node()

# Create components
C = 1 * 10 ^ -9
impedance1 = Resistance(complex(0, -1 / (omega * C)))
source = Source(5)

# Connect nodes
node1.connect_out(impedance1)
node1.connect_in(source)

node2.connect_out(source)
node2.connect_in(impedance1)


# Add to network and solve
network = CircuitSolver(use_complex=True)
network.add_node(node1)
network.add_node(node2)
network.add_component(impedance1)
network.add_component(source)
network.solve(initial_guess=1, ndigits=5)

# Solved results:
print("Node 1", node1.potential.real, "V")
print("Node 2", node2.potential.real, "V")
print("Capacitor 1", impedance1.current.real, "A")
print("Source", source.current.real, "A")
