from interface.Equation import Equation
from interface.SystemOfEquations import SystemOfEquations
from JFNKsolver import JFNKsolver

def round_map(input_map, ndigits):
    rounded_map = {}
    for name, value in input_map.items():
        rounded_map[name] = round(value, ndigits)
    return rounded_map

def print_map(input_map):
    for name, value in input_map.items():
        print(f"{name}: {value}")

system_of_equations = SystemOfEquations()
system_of_equations.add_equation(Equation(["x", "y", "z"], lambda v: v["x"]*v["y"]*v["z"] - 6))
system_of_equations.add_equation(Equation(["x", "y"], lambda v: v["x"] + v["y"] - 3))
system_of_equations.add_equation(Equation(["y", "z"], lambda v: v["y"]**v["z"] - 8))

solver = JFNKsolver(system_of_equations, initial_guess=1)

ndigits = 2
solution_map = solver.solve(verbose = True, rtol = 0, atol = 10**-ndigits, ndigits=ndigits)
solution_map = round_map(solution_map, ndigits)
print_map(solution_map)
