from gui.model.area.Area import Area

class CircleArea(Area):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def render(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def is_touched(self, x, y):
        dist = ((x - self.x) ** 2 + (y - self.y) ** 2) ** (1 / 2)
        return dist <= self.r

    def move_to(self, x, y):
        self.x = x
        self.y = y