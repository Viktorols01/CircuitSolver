from gui.model.area.PointArea import PointArea
from gui.model.GTwopoleSocket import GTwopoleSocket
from gui.model.GTwopole import GTwopole
from circuit.twopoles.Source import Source
from gui.Utility import interpolate

# bridge between two nodes
class GCopper(GTwopole):
    def __init__(self, area_1, area_2):
        self.position_function = lambda: interpolate((area_1.x, area_1.y), (area_2.x, area_2.y), 1 / 2)
        super().__init__(0, 0)

    def _create_area(self, x, y):
        return PointArea(x, y)
    
    def _create_socket_in(self):
        return GTwopoleSocket(self, False, self.position_function)

    def _create_socket_out(self):
        return GTwopoleSocket(self, True, self.position_function)

    def _create_twopole(self):
        return Source(0)

    def render(self, canvas):
        x, y = self.position_function()
        self.area.move_to(x, y)
        pass