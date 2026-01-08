from gui.Utility import interpolate
from gui.sub.GUISocket import GUISocket
from gui.abstract.GUIDraggable import GUIDraggable
from circuit.components.Source import Source

# When two nodes are connected, there needs to be a component between them.
# This is it.
# TODO: Remove this and make only one of the connected nodes add a shared variable.
class GUISilentNode(GUIDraggable):
    def __init__(self, socket_in_outer, socket_out_outer):
        self.math_component = Source(0)

        self.socket_in_outer = socket_in_outer
        self.socket_out_outer = socket_out_outer

        socket1 = GUISocket(
            self,
            lambda: interpolate(
                self.socket_in_outer.positionfunction(),
                self.socket_out_outer.positionfunction(),
                1 / 2,
            ),
            1,
        )
        socket2 = GUISocket(
            self,
            lambda: interpolate(
                self.socket_in_outer.positionfunction(),
                self.socket_out_outer.positionfunction(),
                1 / 2,
            ),
            1,
        )
        super().__init__(0, 0, 0, 0, [socket1, socket2])

    def render(self, canvas):
        # (x, y) = interpolate(
        #     self.socket_in_outer.positionfunction(),
        #     self.socket_out_outer.positionfunction(),
        #     1 / 2,
        # )
        # canvas.create_oval(x - 20, y - 20, x + 20, y + 20)
        self.render_sockets(canvas, current=self.math_component.get_current())
