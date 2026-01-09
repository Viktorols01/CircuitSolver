from gui.abstract.GUIDraggable import GUIRect
from gui.sub.GUISocket import GUISocket
from circuit.nodes.Node import Node
from gui.Utility import interpolate


class GUINode(GUIRect):
    def __init__(self, x, y):
        super().__init__(x, y, self.socket.r, self.socket.r)
        self.self_socket = GUISocket()
        self.sockets = []
        renderframe = 0

    def render(self, canvas):
        self.render_node(canvas)
        self.render_sockets(canvas)
    
    def render_node(self, canvas):


    # responsible for rendering electrons and connections
    def render_sockets(self, canvas, current=0):
        for socket in self.sockets:
            sx, sy = socket.positionfunction()

            socket.render(canvas, sx, sy)

            if render_lines:
                for socket2 in socket.get_sockets():
                    sx2, sy2 = socket2.positionfunction()
                    canvas.create_line(sx, sy, sx2, sy2)

                    # Create moving electrons
                    electron_count = round(
                        ((sx - sx2) ** 2 + (sy - sy2) ** 2) ** 0.5 / 10
                    )
                    if socket == self.get_socket_in():
                        direction = -1
                    else:
                        direction = 1
                    for i in range(electron_count):
                        x, y = interpolate(
                            (sx, sy),
                            (sx2, sy2),
                            (
                                (i + (self.renderframe / 60) * current * direction)
                                % electron_count
                            )
                            / electron_count,
                        )
                        canvas.create_oval(
                            x - 1, y - 1, x + 1, y + 1, fill="#fff", outline="#fff"
                        )
                self.renderframe += 1