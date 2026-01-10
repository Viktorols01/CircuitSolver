from abc import ABC, abstractmethod

class Twopole(ABC):
    def __init__(self):
        self.current = 0
        self.node_in = None
        self.node_out = None

    @abstractmethod
    def get_function(self, potential_out_name, potential_in_name, current_name):
        pass
