from gui.Utility import interpolate


class GUISocketElement:
    def __init__(self, sockets):
        self.sockets = sockets
        self.renderframe = 0

    def render_sockets(self, canvas, render_lines=True, current=0):
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

    def touched_socket(self, x, y):
        for socket in self.sockets:
            sx, sy = socket.positionfunction()
            dist = ((x - sx) ** 2 + (y - sy) ** 2) ** (1 / 2)
            if dist <= 2 * socket.r:
                return (True, socket)
        return (False, None)

    def is_two_pole(self):
        return len(self.sockets) == 2

    def get_socket_in(self):
        if self.is_two_pole():
            return self.sockets[0]

    def get_socket_out(self):
        if self.is_two_pole():
            return self.sockets[1]
        else:
            raise Exception("Socket is not two-pole!")
