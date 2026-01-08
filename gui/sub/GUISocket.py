# transform takes x, y and returns sx, sy
# connection is the connected connection


class GUISocket:
    def __init__(self, component, positionfunction, max_connections):
        self.component = component
        self.positionfunction = positionfunction
        self.max_connections = max_connections

        self.connected_sockets = []

        self.r = 5

    def add_connection(self, socket):
        if not self.can_connect():
            raise Exception("Max connections exceeded!")
        self.connected_sockets.append(socket)

    def get_sockets(self):
        return self.connected_sockets

    def can_connect(self):
        return len(self.connected_sockets) < self.max_connections

    def render(self, canvas, x, y):
        if self.can_connect():
            canvas.create_oval(x - self.r, y - self.r, x + self.r, y + self.r)
