import tkinter as tk

from gui.GUIDiode import GUIDiode
from gui.GUINode import GUINode
from gui.GUIResistance import GUIResistance
from gui.GUISilentNode import GUISilentNode
from gui.GUISource import GUISource


class Window:
    def __init__(self, width, height, solve):
        self.root = tk.Tk()
        self.root.title("CircuitSolver")

        self.is_creating_connection = False
        self.connecting_socket = None
        self.current_x = 0
        self.current_y = 0
        self.held_x = 0
        self.held_y = 0
        self.held_offset_x = 0
        self.held_offset_y = 0

        self.draggables = []
        resistance_button = tk.Button(
            self.root,
            text="Resistance",
            command=lambda: self.draggables.append(GUIResistance(20, 20)),
        )
        resistance_button.pack()
        source_button = tk.Button(
            self.root,
            text="Source",
            command=lambda: self.draggables.append(GUISource(20, 20)),
        )
        source_button.pack()
        source_button = tk.Button(
            self.root,
            text="Diode",
            command=lambda: self.draggables.append(GUIDiode(20, 20)),
        )
        source_button.pack()

        source_button = tk.Button(self.root, text="Solve", command=lambda: solve(self))
        source_button.pack()

        self.canvas = tk.Canvas(self.root, background="red", width=width, height=height)
        self.canvas.pack()

        self.canvas.bind("<Motion>", self.__motion)
        self.canvas.bind("<Button-1>", self.__clicked_left)
        self.canvas.bind("<B1-Motion>", self.__moved_left)
        self.canvas.bind("<ButtonRelease-1>", self.__released_left)
        self.canvas.bind("<Button-3>", self.__clicked_right)
        self.canvas.bind("<B3-Motion>", self.__moved_right)
        self.canvas.bind("<ButtonRelease-3>", self.__released_right)

        self.root.after(10, self.render)
        self.root.mainloop()

    def __motion(self, event):
        pass

    def __clicked_left(self, event):
        self.current_x = event.x
        self.current_y = event.y
        self.held_x = event.x
        self.held_y = event.y

        for draggable in self.draggables:
            touch_socket, touched_socket = draggable.touched_socket(event.x, event.y)
            if touch_socket:
                if touched_socket.can_connect():
                    self.is_creating_connection = True
                    self.connecting_socket = touched_socket
                    return

    def __moved_left(self, event):
        self.current_x = event.x
        self.current_y = event.y

    def __released_left(self, event):
        def connect(socket1, socket2):
            socket1.add_connection(socket2)
            socket2.add_connection(socket1)

        def connect_with_silent_node(socket1, socket2):
            silentnode = GUISilentNode(socket1, socket2)
            connect(socket1, silentnode.sockets[0])
            connect(silentnode.sockets[1], socket2)
            self.draggables.append(silentnode)

        if self.is_creating_connection:
            self.is_creating_connection = False
            at_reasonable_distance = (self.current_x - self.held_x) ** 2 + (
                self.current_y - self.held_y
            ) ** 2 > 100
            if at_reasonable_distance:
                for draggable in self.draggables:
                    touch_socket, touched_socket = draggable.touched_socket(
                        event.x, event.y
                    )
                    if touch_socket:
                        # Connect to component
                        if isinstance(
                            self.connecting_socket.component, GUINode
                        ) and isinstance(touched_socket.component, GUINode):
                            connect_with_silent_node(
                                self.connecting_socket, touched_socket
                            )
                        elif isinstance(
                            self.connecting_socket.component, GUINode
                        ) or isinstance(touched_socket.component, GUINode):
                            connect(self.connecting_socket, touched_socket)
                        return
                # Connect to new node
                node = GUINode(self.current_x, self.current_y)
                if isinstance(self.connecting_socket.component, GUINode):
                    connect_with_silent_node(self.connecting_socket, node.socket)
                else:
                    connect(self.connecting_socket, node.socket)
                self.draggables.append(node)
                return

    def __clicked_right(self, event):
        self.current_x = event.x
        self.current_y = event.y
        self.held_x = event.x
        self.held_y = event.y

        for draggable in self.draggables:
            if draggable.touched(event.x, event.y):
                self.held_offset_x = event.x - draggable.x
                self.held_offset_y = event.y - draggable.y
                draggable.is_dragged = True
                return

    def __moved_right(self, event):
        self.current_x = event.x
        self.current_y = event.y

        for draggable in self.draggables:
            if draggable.is_dragged:
                draggable.move(
                    event.x - self.held_offset_x, event.y - self.held_offset_y
                )
                return

    def __released_right(self, event):
        for draggable in self.draggables:
            if draggable.is_dragged:
                draggable.is_dragged = False

    def render(self):
        self.canvas.delete("all")
        for draggable in self.draggables:
            draggable.render(self.canvas)

        if self.is_creating_connection:
            self.canvas.create_line(
                self.held_x, self.held_y, self.current_x, self.current_y, dash=(2, 2)
            )
            self.connecting_socket.render(self.canvas, self.current_x, self.current_y)

        self.canvas.pack()
        self.root.after(10, self.render)
