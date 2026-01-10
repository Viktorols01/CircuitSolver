from abc import ABC, abstractmethod

class Area(ABC):
    @abstractmethod
    def render(self, canvas):
        pass

    @abstractmethod
    def is_touched(self, x, y):
        pass
    
    @abstractmethod
    def move_to(self, x, y):
        pass