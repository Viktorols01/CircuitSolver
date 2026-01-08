from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self):
        self.current = 0
        self.current = 0
        self.sockets = {"in": None, "out": None}

    def get_type(self):
        return self.type

    def get_sockets(self):
        return self.sockets

    def set_current(self, current):
        self.current = current

    def get_function(self, u_out_name, u_in_name, i_name):
        pass
