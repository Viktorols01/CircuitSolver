from gui.model.area.CircleArea import CircleArea

class GTwopoleSocket:
    def __init__(self, parent, is_out, position_function):
        x, y = position_function()
        self.area = CircleArea(x, y, 10)

        self.parent = parent
        self.is_out = is_out
        self.position_function = position_function

        self.is_connected = False
    
    def update_position(self):
        x, y = self.position_function()
        self.area.x = x
        self.area.y = y

    def render(self, canvas):
        if not self.is_connected:
            self.area.render(canvas)
