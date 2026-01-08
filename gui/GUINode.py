from gui.abstract.GUIDraggable import GUIDraggable
from gui.sub.GUISocket import GUISocket
from circuit.nodes.Node import Node


class GUINode(GUIDraggable):
    def __init__(self, x, y):
        self.math_node = Node()

        self.socket = GUISocket(
            self, lambda: (self.x + self.w / 2, self.y + self.h / 2), 7
        )
        super().__init__(x, y, self.socket.r, self.socket.r, [self.socket])

    def render(self, canvas):
        self.render_sockets(canvas, render_lines=False)
