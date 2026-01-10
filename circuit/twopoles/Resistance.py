from circuit.Twopole import Twopole

class Resistance(Twopole):
    def __init__(self, R):
        super().__init__()
        self.R = R

    def get_function(self, potential_out_name, potential_in_name, current_name):
        return lambda x: (x[potential_in_name] - x[potential_out_name]) / self.R - x[current_name]
