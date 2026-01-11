from circuit.Node import Node
from circuit.CircuitSolver import CircuitSolver

from circuit.twopoles.Resistance import Resistance
from circuit.twopoles.Source import Source
from circuit.twopoles.Diode import Diode

# Create nodes
node1 = Node()
node2 = Node()
node3 = Node()

# Create components
resistance = Resistance(10)
diode = Diode()
source = Source(2)

# Connect nodes
node1.connect_in(source)
node1.connect_out(resistance)

node2.connect_in(resistance)
node2.connect_out(diode)

node3.connect_in(diode)
node3.connect_out(source)

# Add to network and solve
network = CircuitSolver()
network.add_node(node1)
network.add_node(node2)
network.add_node(node3)
network.add_twopole(resistance)
network.add_twopole(source)
network.add_twopole(diode)
network.solve(initial_guess=1, ndigits=2)

# Solved results:
print("Node 1", node1.potential, "V")
print("Node 2", node2.potential, "V")
print("Node 3", node3.potential, "V")
print("Resistance 1", resistance.current, "A")
print("Source", source.current, "A")
print("Diode", diode.current, "A")
