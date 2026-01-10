from abc import ABC, abstractmethod

class GTwopole(ABC):
    def __init__(self, x, y):
        self.area = self._create_area(x, y)
        self.socket_in = self._create_socket_in()
        self.socket_out = self._create_socket_out()
        self.twopole = self._create_twopole()

    @abstractmethod
    def _create_area(self, x, y):
        pass
    
    @abstractmethod
    def _create_socket_in(self):
        pass
    
    @abstractmethod
    def _create_socket_out(self):
        pass

    @abstractmethod
    def _create_twopole(self):
        pass

    @abstractmethod
    def render(self, canvas):
        pass

    def render_sockets(self, canvas):
        self.socket_in.render(canvas)
        self.socket_out.render(canvas)
    
    def update_socket_positions(self):
        self.socket_in.update_position()
        self.socket_out.update_position()