from circuit.nodes.Node import Node
from circuit.CircuitSolver import CircuitSolver

from circuit.components.Resistance import Resistance
from circuit.components.Source import Source
from circuit.components.Diode import Diode

# Create nodes
node1 = Node()
node2 = Node()
node3 = Node()

# Create components
resistance1 = Resistance(2)
resistance2 = Resistance(2)
diode = Diode()
source = Source(10)

# Connect nodes
node1.connect_in(source)
node1.connect_out(resistance1)
node1.connect_out(resistance2)

node2.connect_in(resistance1)
node2.connect_in(resistance2)
node2.connect_out(diode)

node3.connect_in(diode)
node3.connect_out(source)

# Add to network and solve
network = CircuitSolver()
network.add_node(node1)
network.add_node(node2)
network.add_node(node3)
network.add_twopole(resistance1)
network.add_twopole(resistance2)
network.add_twopole(source)
network.add_twopole(diode)
network.solve(initial_guess=0.001, ndigits=2)

# Solved results:
print("Node 1", node1.potential, "V")
print("Node 2", node2.potential, "V")
print("Node 3", node3.potential, "V")
print("Resistance 1", resistance1.current, "A")
print("Resistance 2", resistance2.current, "A")
print("Source", source.current, "A")
print("Diode", diode.current, "A")
