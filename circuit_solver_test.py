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
resistance = Resistance(2)
source = Source(10)

# Connect nodes
node1.connect_in(source)
node1.connect_out(resistance)

node2.connect_in(resistance)
node2.connect_out(source)

# Add to network and solve
network = CircuitSolver()
network.add_node(node1)
network.add_node(node2)
network.add_component(resistance)
network.add_component(source)
network.solve(initial_guess=1, ndigits=2)

# Solved results:
print("Node 1", node1.potential, "V")
print("Node 2", node2.potential, "V")
print("Resistance", resistance.current, "A")
print("Source", source.current, "A")
