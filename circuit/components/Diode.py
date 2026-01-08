import numpy as np


class Diode:
    def __init__(self, Is=0.01):
        self.Is = Is

        # Thermal voltage
        self.V_thermal = 25.9 * 10**-3

        self.current = 0
        self.sockets = {"in": None, "out": None}

    def get_type(self):
        return self.type

    def get_sockets(self):
        return self.sockets

    def set_current(self, current):
        self.current = current

    def get_current(self):
        return self.current

    # u_in, u_out, i
    def get_function(self, u_out_name, u_in_name, i_name):
        return lambda x: self.Is * (np.exp((x[u_out_name] - x[u_in_name]) / self.V_thermal) - 1) - x[i_name]
