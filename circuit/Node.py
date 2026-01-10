class Node:
    def __init__(self):
        self.twopoles_in = []
        self.twopoles_out = []
        self.potential = 0

    def connect_in(self, component):
        self.twopoles_in.append(component)
        component.node_out = self

    def connect_out(self, component):
        self.twopoles_out.append(component)
        component.node_in = self