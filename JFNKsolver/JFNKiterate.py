import numpy as np
import scipy

class JFNKiterate:
    def __init__(self, system_of_equations, initial_guess=1, dtype=float):
        self.system_of_equations = system_of_equations
        self.n = len(system_of_equations.equations)
        self.dtype = dtype
        self.__vectorize(initial_guess)

    def __vectorize(self, initial_guess):
        self.vector = np.zeros(shape=[self.n], dtype=self.dtype)
        self.name_to_index = {}
        i = 0
        for name in self.system_of_equations.get_variable_names():
            self.vector[i] = initial_guess
            self.name_to_index[name] = i
            i += 1

    def get_vector(self):
        return self.vector
    
    def add_vector(self, dv):
        self.vector += dv

    def get_residual(self, u = None):
        evaluation_map = self.get_value_map_from_vector(u)
        residual = np.zeros(shape=[self.n], dtype=self.dtype)
        for i in range(self.n):
            residual[i] = self.system_of_equations.evaluate_equation(i, evaluation_map)
        return residual

    # function to calculate the directional derivative in a specific direction q
    def get_directional_derivative(self, q):
        if np.linalg.norm(q) == 0:
            epsilon = 10**-7
        else:
            epsilon = 10**-7 / np.sqrt(np.linalg.norm(q))

        u0 = self.get_vector()
        u1 = u0 + q * epsilon

        # represents the jacobian multiplied by q
        directional_derivative = (
            self.get_residual(u1) - self.get_residual(u0)
        ) / epsilon
        return directional_derivative

    def get_value_map_from_vector(self, u = None):
        if u is None:
            u = self.get_vector()

        value_map = {}
        for name in self.system_of_equations.get_variable_names():
            index = self.name_to_index[name]
            value_map[name] = u[index]
        return value_map
