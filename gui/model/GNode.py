from gui.Utility import interpolate
from gui.model.area.CircleArea import CircleArea
from gui.model.gtwopoles.GCopper import GCopper
from circuit.Node import Node

# this code must be written for both nodes and components as both have sockets
# (nodes have many, components have in and out)
class GNode:
    def __init__(self, x, y):
        self.area = CircleArea(x, y, 10)
        self.gtwopole_sockets_in = []
        self.gtwopole_sockets_out = []
        self.node = Node()

        self.render_frame = 0

    def add_socket_in(self, socket):
        self.gtwopole_sockets_in.append(socket)

    def add_socket_out(self, socket):
        self.gtwopole_sockets_out.append(socket)
    
    def render(self, canvas):
        self.area.render(canvas)
        self.render_connections(canvas)

    # responsible for rendering electrons and connections
    def render_connections(self, canvas):
        for socket_in in self.gtwopole_sockets_in:
            self.render_connection(canvas, socket_in, direction=-1)
        for socket_out in self.gtwopole_sockets_out:
            self.render_connection(canvas, socket_out, direction=1)

    def render_connection(self, canvas, socket, direction):
        canvas.create_line(self.area.x, self.area.y, socket.area.x, socket.area.y)

        # Create moving electrons
        current = socket.parent.twopole.current
        electron_count = round(
            ((socket.area.x - self.area.x) ** 2 + (socket.area.y - self.area.y) ** 2) ** 0.5 / 10
        )
        for i in range(electron_count):
            speed_factor = 1/20
            x, y = interpolate(
                (socket.area.x, socket.area.y),
                (self.area.x, self.area.y),
                (
                    (i + (self.render_frame * speed_factor) * current * direction)
                    % electron_count
                )
                / electron_count,
            )
            canvas.create_oval(x - 1, y - 1, x + 1, y + 1, fill="#fff", outline="#fff")
        self.render_frame += 1
    
    def update_copper_positions(self):
        for socket in self.gtwopole_sockets_in + self.gtwopole_sockets_out:
            parent = socket.parent
            if isinstance(parent, GCopper):
                parent.update_position()
