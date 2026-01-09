from gui.abstract.GUIDraggable import GUIRect
from gui.sub.GUISocket import GUISocket
from circuit.components.Source import Source


class GUISource(GUIRect):
    def __init__(self, x, y):
        self.math_component = Source(5)

        socket1 = GUISocket(self, lambda: (self.x + self.w / 2, self.y + self.h), 1)
        socket2 = GUISocket(self, lambda: (self.x + self.w / 2, self.y), 1)
        super().__init__(x, y, 20, 100, [socket1, socket2])

    def render(self, canvas):
        self.render_hitbox(canvas)
        canvas.create_rectangle(
            self.x,
            self.y,
            self.x + self.w,
            self.y + self.h,
            fill="white",
            outline="black",
            width=2,
        )
        canvas.create_text((self.x + self.w / 2, self.y + 10), text="+")
        canvas.create_text((self.x + self.w / 2, self.y + self.h - 10), text="-")
        self.render_sockets(canvas, current=self.math_component.get_current())
