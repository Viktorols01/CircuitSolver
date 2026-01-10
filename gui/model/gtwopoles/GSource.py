from gui.model.area.RectArea import RectArea
from gui.model.GTwopoleSocket import GTwopoleSocket
from gui.model.GTwopole import GTwopole
from circuit.twopoles.Source import Source

class GSource(GTwopole):
    def __init__(self, x, y):
        self.w = 20
        self.h = 100
        super().__init__(x, y)

    def _create_area(self, x, y):
        return RectArea(x, y, self.w, self.h)
    
    def _create_socket_in(self):
        # out might be in lol, check graphics 
        return GTwopoleSocket(self, False, lambda: (self.area.x + self.w / 2, self.area.y + self.h))

    def _create_socket_out(self):
        return GTwopoleSocket(self, True, lambda: (self.area.x + self.w / 2, self.area.y))

    def _create_twopole(self):
        return Source(5)

    def render(self, canvas):
        canvas.create_rectangle(
            self.area.x,
            self.area.y,
            self.area.x + self.area.w,
            self.area.y + self.area.h,
            fill="white",
            outline="black",
            width=2,
        )
        canvas.create_text((self.area.x + self.area.w / 2, self.area.y + 10), text="+")
        canvas.create_text((self.area.x + self.area.w / 2, self.area.y + self.area.h - 10), text="-")
