from JFNKsolver.interface.SystemOfEquations import SystemOfEquations
from JFNKsolver.interface.Equation import Equation
from JFNKsolver.JFNKsolver import JFNKsolver


class SolverNetwork:
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

        variable_map = solver.solve(verbose=verbose, ndigits=ndigits)
        for name, value in variable_map.items():
            if name in self.node_map:
                self.node_map[name].set_potential(value)
            else:
                self.component_map[name].set_current(value)

    def __add_node_equations(self, system_of_equations):

        grounded = False
        for node_name, node in self.node_map.items():
            print(node_name)
            # ground first node
            if not grounded:
                equation = Equation([node_name], lambda x: x[node_name] - 0)
                system_of_equations.add_equation(equation)
                grounded = True
                continue

            connections = node.get_connections()
            n = len(connections)
            sign_list = []
            name_list = []
            for pair in connections:
                component, socket = pair
                if socket == "in":
                    sign_list.append(-1)
                elif socket == "out":
                    sign_list.append(1)
                else:
                    raise Exception("socket is not 'in' or 'our'")

                name_list.append(component.name)

            def function(x, name_list_, sign_list_, n_):
                sum = 0
                for j in range(n_):
                    name = name_list_[j]
                    sum += sign_list_[j] * x[name]
                return sum

            # kirchoffs first law
            # viktigt: early binding!
            equation = Equation(name_list, lambda x, nl=name_list, s=sign_list, t=n: function(x, nl, s, t))
            print("b")
            system_of_equations.add_equation(equation)

    def __add_component_equations(self, system_of_equations):
        for name, component in self.component_map.items():
            node_in = component.get_sockets()["in"]
            name_in = node_in.name

            node_out = component.get_sockets()["out"]
            name_out = node_out.name

            equation = Equation([name_in, name_out, name], component.get_function(name_in, name_out, name))
            system_of_equations.add_equation(equation)
