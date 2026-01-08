class Node:
    def __init__(self):
        self.connections = []
        self.potential = 0

    def set_potential(self, potential):
        self.potential = potential

    def get_potential(self):
        return self.potential

    def get_connections(self):
        return self.connections

    def connect_to(self, component, socket):
        self.connections.append((component, socket))

        component.sockets[socket] = self

    def reset(self):
        self.connections = []
        self.potential = 0

    # --- DEBUG ---
    def print(self, name, ndigits = 0):
        print("Node ", name)
        if self.potential_known:
            print("\tPotential (set):", round(self.potential, ndigits),"V")
        else:
            print("\tPotential:", round(self.potential, ndigits),"V")
        if self.current_known:
            print("\tCurrent (set):", round(self.current, ndigits), "A")
        else:
            print("\tCurrent:", round(self.current, ndigits), "A")
        #print("\tFunction:", self.function())