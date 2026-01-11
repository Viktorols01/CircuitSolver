from gui.model.area.RectArea import RectArea
from gui.model.GTwopoleSocket import GTwopoleSocket
from gui.model.GTwopole import GTwopole
from circuit.twopoles.Resistance import Resistance

class GResistance(GTwopole):
    def __init__(self, x, y):
        self.w = 100
        self.h = 40
        super().__init__(x, y)

    def _create_area(self, x, y):
        return RectArea(x, y, self.w, self.h)
    
    def _create_socket_in(self):
        # out might be in lol, check graphics 
        return GTwopoleSocket(self, False, lambda: (self.area.x, self.area.y + self.h / 2))

    def _create_socket_out(self):
        return GTwopoleSocket(self, True, lambda: (self.area.x + self.w, self.area.y + self.h / 2))

    def _create_twopole(self):
        return Resistance(1)

    def render(self, canvas):
        #self.area.render(canvas)
        canvas.create_rectangle(
            self.area.x,
            self.area.y,
            self.area.x + self.area.w,
            self.area.y + self.area.h,
            fill="white",
            outline="black",
            width=2,
        )
