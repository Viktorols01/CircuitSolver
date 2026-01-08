from JFNKsolver.interface.SystemOfEquations import SystemOfEquations
from JFNKsolver.interface.Equation import Equation
from JFNKsolver.JFNKsolver import JFNKsolver


class CircuitSolver:
    def __init__(self, use_complex=False):
        self.use_complex = use_complex

        self.node_map = {}
        self.node_count = 0
        self.component_map = {}
        self.component_count = 0

    def add_node(self, node):
        name = f"n{self.node_count}"
        self.node_map[name] = node
        # ducktyping comes in handy but this is a crime
        node.name = name
        self.node_count += 1

    def add_component(self, component):
        name = f"c{self.component_count}"
        self.component_map[name] = component
        # ducktyping comes in handy but this is a crime
        component.name = name
        self.component_count += 1

    def solve(self, verbose=False, initial_guess=1, ndigits=2):
        system_of_equations = SystemOfEquations()
        self.__add_node_equations(system_of_equations)
        self.__add_component_equations(system_of_equations)
        system_of_equations.assert_is_balanced()

        if self.use_complex:
            dtype=complex
        else:
            dtype=float
        solver = JFNKsolver(system_of_equations, initial_guess=initial_guess, dtype=dtype)

        variable_map = solver.solve(verbose=verbose, rtol=0.01, atol=0, ndigits=ndigits)
        for name, value in variable_map.items():
            if name in self.node_map:
                self.node_map[name].potential = value
            else:
                self.component_map[name].current = value

    def __add_node_equations(self, system_of_equations):
        grounded = False
        for node_name, node in self.node_map.items():
            # ground first node
            if not grounded:
                equation = Equation([node_name], lambda x: x[node_name] - 0)
                system_of_equations.add_equation(equation)
                grounded = True
                continue

            sign_list = []
            name_list = []
            for component_in in node.components_in:
                sign_list.append(-1)
                name_list.append(component_in.name)

            for component_out in node.components_out:
                sign_list.append(1)
                name_list.append(component_out.name)

            # kirchoffs first law
            # important: early binding!
            def kirchoff_residual(x, name_list_, sign_list_):
                sum = 0
                for j in range(len(name_list_)):
                    name = name_list_[j]
                    sum += sign_list_[j] * x[name]
                return sum

            equation = Equation(name_list, lambda x, nl=name_list, sl=sign_list: kirchoff_residual(x, nl, sl))
            system_of_equations.add_equation(equation)

    def __add_component_equations(self, system_of_equations):
        for name, component in self.component_map.items():
            name_out = component.node_out.name
            name_in = component.node_in.name
            equation = Equation([name_out, name_in, name], component.get_function(name_out, name_in, name))
            system_of_equations.add_equation(equation)