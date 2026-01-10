from circuit.CircuitSolver import CircuitSolver
from circuit.twopoles.Resistance import Resistance
from circuit.twopoles.Source import Source
from circuit.Node import Node

from gui.model.GNode import GNode
from gui.model.gtwopoles.GCopper import GCopper

class GCircuitSolverModel:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dragged_x = 0
        self.dragged_y = 0
        self.dragged_offset_x = 0
        self.dragged_offset_y = 0
        self.dragged_area = None
        self.dragged_twopole = None

        self.connecting_gtwopole_socket = None
        self.connecting_gnode = None

        self.gtwopoles = []
        self.gnodes = []
    
    def add_twopole(self, twopole):
        self.gtwopoles.append(twopole)

    def add_node(self, node):
        self.gnodes.append(node)

    def handle_start_connecting(self):
        def handle_gtwopole_socket_start_connecting(gtwopole):
            def handle_socket_start_connecting(socket):
                if socket.area.is_touched(self.x, self.y):
                        self.connecting_gtwopole_socket = socket
                        return True
                return False
            return handle_socket_start_connecting(gtwopole.socket_in) or handle_socket_start_connecting(gtwopole.socket_out)
        
        def handle_gnode_start_connecting(gnode):
            if gnode.area.is_touched(self.x, self.y):
                self.connecting_gnode = gnode
                return True
            return False
        
        for gtwopole in self.gtwopoles:
            if handle_gtwopole_socket_start_connecting(gtwopole):
                return 
        
        for gnode in self.gnodes:
            if handle_gnode_start_connecting(gnode):
                return

    def handle_stop_connecting(self):
        at_reasonable_distance = (self.x - self.dragged_x) ** 2 + (self.y - self.dragged_y) ** 2 > 100
        if not at_reasonable_distance:
            self.connecting_gnode = None
            self.connecting_gtwopole_socket = None
            return

        if self.connecting_gnode:
            self._connect_gnode(self.connecting_gnode)
            self.connecting_gnode = None
        if self.connecting_gtwopole_socket:
            self._connect_gtwopole_socket(self.connecting_gtwopole_socket)
            self.connecting_gtwopole_socket = None

    def _connect_gnode_to_socket(self, gnode, gtwopole_socket):
        if gtwopole_socket.is_out:
            gnode.add_socket_out(gtwopole_socket)
        else:
            gnode.add_socket_in(gtwopole_socket)
            

    def _connect_gnode(self, gnode):
        def create_gcopper(gnode, other_gnode):
            gcopper = GCopper(gnode.area, other_gnode.area)
            self._connect_gnode_to_socket(gnode, gcopper.socket_in)
            self._connect_gnode_to_socket(other_gnode, gcopper.socket_out)
            self.gtwopoles.append(gcopper)
            
        touched_gtwopole_socket_out = self._get_touched_gtwopole_socket_out()
        if touched_gtwopole_socket_out:
            gnode.gtwopole_sockets_out.append(touched_gtwopole_socket_out)
            return

        touched_gtwopole_socket_in = self._get_touched_gtwopole_socket_in()
        if touched_gtwopole_socket_in:
            gnode.gtwopole_sockets_in.append(touched_gtwopole_socket_in)
            return

        touched_gnode = self._get_touched_gnode()
        if touched_gnode:
            create_gcopper(gnode, touched_gnode)
            return
        
        created_gnode = GNode(self.x, self.y)
        create_gcopper(gnode, created_gnode)
        self.gnodes.append(created_gnode)

    def _connect_gtwopole_socket(self, gtwopole_socket):
        def create_connecting_gnode(gtwopole_socket, other_gtwopole_socket):
            gnode = GNode(self.x, self.y)
            self._connect_gnode_to_socket(gnode, gtwopole_socket)
            self._connect_gnode_to_socket(gnode, other_gtwopole_socket)
            self.gnodes.append(gnode)
            
        touched_gtwopole_socket_out = self._get_touched_gtwopole_socket_out()
        if touched_gtwopole_socket_out:
            create_connecting_gnode(gtwopole_socket, touched_gtwopole_socket_out)
            return

        touched_gtwopole_socket_in = self._get_touched_gtwopole_socket_in()
        if touched_gtwopole_socket_in:
            create_connecting_gnode(gtwopole_socket, touched_gtwopole_socket_in)
            return

        touched_gnode = self._get_touched_gnode()
        if touched_gnode:
            self._connect_gnode_to_socket(touched_gnode, gtwopole_socket)
            return
        
        created_gnode = GNode(self.x, self.y)
        self._connect_gnode_to_socket(created_gnode, gtwopole_socket)
        self.gnodes.append(created_gnode)

    def pickup_dragged_area(self):
        for gtwopole in self.gtwopoles:
            area = gtwopole.area
            if area.is_touched(self.x, self.y):
                self.dragged_x = self.x
                self.dragged_y = self.y
                self.dragged_offset_x = self.x - area.x
                self.dragged_offset_y = self.y - area.y
                self.dragged_area = area
                self.dragged_twopole = gtwopole
                return
        for gnode in self.gnodes:
            area = gnode.area
            if area.is_touched(self.x, self.y):
                self.dragged_x = self.x
                self.dragged_y = self.y
                self.dragged_offset_x = self.x - area.x
                self.dragged_offset_y = self.y - area.y
                self.dragged_area = area
                return

    def move_dragged_area(self):
        # borde också uppdatera sockets på något jävla sätt
        if self.dragged_area:
            self.dragged_area.move_to(self.x - self.dragged_offset_x, self.y - self.dragged_offset_y)
        if self.dragged_twopole:
            self.dragged_twopole.update_socket_positions()
    
    def release_dragged_area(self):
        self.dragged_area = None
        self.dragged_twopole = None
    
    def update_position(self, x, y):
        self.x = x
        self.y = y
    
    def update_dragged_position(self, x, y):
        self.dragged_x = x
        self.dragged_y = y

    def render(self, canvas):
        for gtwopole in self.gtwopoles:
            gtwopole.render(canvas)
            gtwopole.render_sockets(canvas)

        for gnode in self.gnodes:
            gnode.render(canvas)

        if self.connecting_gnode or self.connecting_gtwopole_socket:
            canvas.create_line(self.dragged_x, self.dragged_y, self.x, self.y, dash=(2, 2))

    def solve(self):
        network = CircuitSolver()
        for gtwopole in self.gtwopoles:
            network.add_twopole(gtwopole.twopole)

        nodes = []
        for gnode in self.gnodes:
            node = gnode.node
            for gtwopole_socket_in in gnode.gtwopole_sockets_in:
                twopole = gtwopole_socket_in.parent.twopole
                node.connect_in(twopole)
            for gtwopole_socket_out in gnode.gtwopole_sockets_out:
                twopole = gtwopole_socket_out.parent.twopole
                gnode.node.connect_out(twopole)
            network.add_node(gnode.node)
                
        network.solve(verbose=True, initial_guess=1, ndigits=2)

    def _get_touched_gtwopole_socket_out(self):
        for gtwopole in self.gtwopoles:
            if gtwopole.socket_out.area.is_touched(self.x, self.y):
                return gtwopole.socket_out

        return None

    def _get_touched_gtwopole_socket_in(self):
        for gtwopole in self.gtwopoles:
            if gtwopole.socket_in.area.is_touched(self.x, self.y):
                return gtwopole.socket_in

        return None

    def _get_touched_gnode(self):
        for gnode in self.gnodes:
            if gnode.area.is_touched(self.x, self.y):
                return gnode
