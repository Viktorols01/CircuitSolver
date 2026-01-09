class Socket:
    def __init__(self, x, y, parent, position_function = (lambda x, y: (x, y))):
        self.x = x
        self.y = y
        self.parent = parent
        self.position_function = position_function
    
    def update_position_based_on_parent(self, x, y):
        sx, sy = self.position_function(x, y)
        self.x = sx
        self.y = sy

    def connect_node(self, node):
        self.node = node

    def is_not_connected(self):
        return self.node is None

    def render(self, canvas):
        r = 5
        if self.is_not_connected():
            canvas.create_oval(self.x - r, self.y - r, self.x + r, self.y + r)