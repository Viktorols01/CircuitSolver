from gui.abstract.GUISocketElement import GUISocketElement

# alltid rektangulära, men sockets kan vara på olika positioner


class GUIDraggable(GUISocketElement):
    def __init__(self, x, y, w, h, sockets):
        super().__init__(sockets)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.is_dragged = False

    def render_base(self, canvas):
        canvas.create_rectangle(
            self.x,
            self.y,
            self.x + self.w,
            self.y + self.h,
            outline="black",
            width=1,
        )

    def touched(self, x, y):
        if x > self.x and x < self.x + self.w:
            if y > self.y and y < self.y + self.h:
                return True
        return False

    def move(self, x, y):
        self.x = x
        self.y = y
