from gui.model.area.RectArea import RectArea
from gui.model.GTwopoleSocket import GTwopoleSocket
from gui.model.GTwopole import GTwopole
from circuit.twopoles.Diode import Diode

class GDiode(GTwopole):
    def __init__(self, x, y):
        self.w = 80
        self.h = 80
        super().__init__(x, y)

    def _create_area(self, x, y):
        return RectArea(x, y, self.w, self.h)
    
    def _create_socket_in(self):
        # out might be in lol, check graphics 
        return GTwopoleSocket(self, False, lambda: (self.area.x, self.area.y + self.h / 2))

    def _create_socket_out(self):
        return GTwopoleSocket(self, True, lambda: (self.area.x + self.w, self.area.y + self.h / 2))

    def _create_twopole(self):
        return Diode()

    def render(self, canvas):
        points = [
            self.area.x,
            self.area.y,
            self.area.x + self.area.w,
            self.area.y + self.area.h / 2,
            self.area.x,
            self.area.y + self.area.h,
        ]
        canvas.create_polygon(
            points,
            outline="black",
            fill="white",
            width=2,
        )
