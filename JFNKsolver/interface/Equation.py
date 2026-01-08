# a function takes a dictionary with variables as parameter 
# and returns a residual
class Equation:
    def __init__(self, variable_name_set, function):
        # we need variable names to combine equations later
        self.variable_name_set = variable_name_set
        self.function = function

    def get_variable_names():
        return self.variable_name_set

    def evaluate(self, evaluation_map):
        return self.function(evaluation_map)
