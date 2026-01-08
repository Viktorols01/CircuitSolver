class Source:
    def __init__(self, Vs):
        self.Vs = Vs

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

    # # u_in, u_out, i
    def get_function(self, u_out_name, u_in_name, i_name):
        return lambda x: x[u_out_name] + self.Vs - x[u_in_name]
