from circuit.nodes.Node import Node
from circuit.SolverNetwork import Network_solver

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
node1.connect_to(impedance1, "out")
node1.connect_to(source, "in")

node2.connect_to(source, "out")
node2.connect_to(impedance1, "in")


# Add to network and solve
network = Network_solver(complex=True)
network.add_node(node1)
network.add_node(node2)
network.add_component(impedance1)
network.add_component(source)
network.solve(initial_value=1, ndigits=5)

# Solved results:
print("Node 1", node1.get_potential().real, "V")
print("Node 2", node2.get_potential().real, "V")
print("Capacitor 1", impedance1.get_current().imag, "A")
print("Source", source.get_current().imag, "A")
