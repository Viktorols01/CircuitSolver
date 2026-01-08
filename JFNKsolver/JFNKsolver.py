import numpy as np
import scipy

from JFNKsolver.JFNKiterate import JFNKiterate

# Jacobian Free Newton-Krylov
class JFNKsolver:
    def __init__(self, system_of_equations, initial_guess=1, dtype=float):
        self.system_of_equations = system_of_equations
        self.initial_guess = initial_guess
        self.dtype = dtype

    def solve(self, verbose=False, rtol=0, atol=10**-3, ndigits=10):
        iterate = JFNKiterate(self.system_of_equations, self.initial_guess, self.dtype)

        res_init = iterate.get_residual()
        res_init_norm = np.linalg.norm(res_init)
        res = res_init

        du = 0

        k = 0
        while np.linalg.norm(res) > rtol * res_init_norm + atol:
            k += 1
            if verbose:
                print("Newton-Raphson iteration", k)
                print("Residual vector", res)
                print("Residual norm", np.linalg.norm(res))
                print("Variables:")
                for name, value in iterate.get_value_map_from_vector().items():
                    print("\t", name, value)
                print("Previous variable increment", du)

            du = self.__gmresIteration(iterate, verbose=verbose)
            iterate.add_vector(du)

            res = iterate.get_residual()

        if verbose:
            print("Newton-Raphson finished in", k, "iterations.")
            print("Initial norm:", res_init)
            print("Final norm", np.linalg.norm(res))

        return iterate.get_value_map_from_vector()


    # GMRES to find du
    def __gmresIteration(self, iterate, verbose=False):
        n = len(self.system_of_equations.get_variable_names())

        # represents the jacobian
        A = scipy.sparse.linalg.LinearOperator(
            (n, n), matvec=iterate.get_directional_derivative
        )
        b = -iterate.get_residual()
        x0 = iterate.get_vector()
        du, info = scipy.sparse.linalg.gmres(A, b, x0)
        if info != 0:
            print(f"GMRES didn't reach expected minimum in {info} iterations")

        return du
