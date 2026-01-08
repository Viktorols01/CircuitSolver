import numpy as np
from circuit.components.Component import Component

# The diode has problems when solving with high numbers (makes sense).
# If this is to be used, it seems important to use sources with
# low voltages.
class Diode(Component):
    def __init__(self, Is=0.01):
        self.Is = Is
        # Thermal voltage
        self.V_thermal = 25.9 * 10**-3

    def get_function(self, potential_out_name, potential_in_name, current_name):
        return lambda x: self.Is * (np.exp((x[potential_in_name] - x[potential_out_name]) / self.V_thermal) - 1) - x[current_name]
