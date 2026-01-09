# this code must be written for both nodes and components as both have sockets
# (nodes have many, components have in and out)
class SocketList:
    def __init__(self):
        self.sockets = []

    def update_socket_positions_based_on_parent(self, x, y):
        for socket in self.sockets:
            socket.update_position_based_on_parent(x, y)
    
    def render_sockets(self, canvas):
        for socket in self.sockets:
            socket.render(canvas)

    def get_touched_socket(self, x, y):
        for socket in self.sockets:
            sx = socket.x
            sy = socket.y
            dist = ((x - sx) ** 2 + (y - sy) ** 2) ** (1 / 2)
            if dist <= 2 * socket.r:
                return socket
        return None