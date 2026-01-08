class SystemOfEquations:
    def __init__(self):
        # Equations
        self.equations = []
        # Variable names
        self.variable_name_set = set()

    def add_equation(self, equation):    
        self.variable_name_set.update(equation.variable_name_set)
        self.equations.append(equation)
    
    def evaluate_equation(self, i, evaluation_map):
        return self.equations[i].evaluate(evaluation_map)

    def get_variable_names_for_equation(self, i):
        return self.equations[i].get_variable_names()

    def get_variable_names(self):
        return self.variable_name_set

    def assert_is_balanced(self):
        n = len(self.equations)
        m = len(self.variable_name_set)
        assert n <= m, f"more equations ({n}) than variables ({m})"
        assert n >= m, f"more variables ({m}) than equations ({n})"