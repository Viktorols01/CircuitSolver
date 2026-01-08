from gui.GUINode import GUINode
from gui.GUIResistance import GUIResistance
from gui.GUISource import GUISource
from gui.GUISilentNode import GUISilentNode
from gui.Window import Window
from circuit.CircuitSolver import CircuitSolver
from circuit.components.Resistance import Resistance
from circuit.components.Source import Source
from circuit.nodes.Node import Node


def solve(window):
    # Create and connect nodes and components
    nodes = []
    components = []
    for draggable in window.draggables:
        if isinstance(draggable, GUINode):
            # Add node
            draggable.math_node.reset()
            nodes.append(draggable.math_node)

            # Connect node
            for socket in draggable.socket.connected_sockets:
                component = socket.component
                if component.is_two_pole():
                    if socket == component.get_socket_in():
                        draggable.math_node.connect_to(component.math_component, "in")
                    elif socket == component.get_socket_out():
                        draggable.math_node.connect_to(component.math_component, "out")
                    else:
                        raise Exception("Network not connected properly!")
                else:
                    raise Exception("Components is not two-pole!")
        else:
            # Add component
            components.append(draggable.math_component)

    # Add to network
    network = CircuitSolver()
    for node in nodes:
        network.add_node(node)
    for component in components:
        network.add_component(component)

    network.solve(verbose=True, initial_guess=1, ndigits=2)


window = Window(800, 800, lambda window: solve(window))
