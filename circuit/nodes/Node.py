class Node:
    def __init__(self):
        self.components_in = []
        self.components_out = []
        self.potential = 0

    def connect_in(self, component):
        self.components_in.append(component)
        component.node_out = self

    def connect_out(self, component):
        self.components_out.append(component)
        component.node_in = self