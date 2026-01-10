from gui.model.area.Area import Area

class PointArea(Area):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def render(self, canvas):
        pass

    def is_touched(self, x, y):
        return False

    def move_to(self, x, y):
        self.x = x
        self.y = y