# alltid rektangulära hitboxes nu
class GUIRect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def render_hitbox(self, canvas):
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

    def move_to(self, x, y):
        self.x = x
        self.y = y