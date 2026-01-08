from circuit.components.Component import Component

class Source(Component):
    def __init__(self, Vs):
        self.Vs = Vs

    def get_function(self, potential_out_name, potential_in_name, current_name):
        return lambda x: x[potential_out_name] - self.Vs - x[potential_in_name]
