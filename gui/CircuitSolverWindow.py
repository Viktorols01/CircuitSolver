import tkinter as tk

from gui.model.gtwopoles.GCopper import GCopper
from gui.model.gtwopoles.GDiode import GDiode
from gui.model.gtwopoles.GResistance import GResistance
from gui.model.gtwopoles.GSource import GSource

from gui.model.GCircuitSolverModel import GCircuitSolverModel

class CircuitSolverWindow:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.root.title("CircuitSolver")

        self.circuit_solver_model = GCircuitSolverModel()

        resistance_button = tk.Button(
            self.root,
            text="Resistance",
            command=lambda: self.circuit_solver_model.add_twopole(GResistance(20, 20)),
        )
        resistance_button.pack()
        source_button = tk.Button(
            self.root,
            text="Source",
            command=lambda: self.circuit_solver_model.add_twopole(GSource(20, 20)),
        )
        source_button.pack()
        source_button = tk.Button(
            self.root,
            text="Diode",
            command=lambda: self.circuit_solver_model.add_twopole(GDiode(20, 20)),
        )
        source_button.pack()

        source_button = tk.Button(self.root, text="Solve", command=self.circuit_solver_model.solve)
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
        self.circuit_solver_model.update_position(event.x, event.y)

    def __clicked_left(self, event):
        self.circuit_solver_model.update_position(event.x, event.y)
        self.circuit_solver_model.update_dragged_position(event.x, event.y)
        self.circuit_solver_model.pickup_dragged_area()

    def __moved_left(self, event):
        self.circuit_solver_model.update_position(event.x, event.y)
        self.circuit_solver_model.move_dragged_area()

    def __released_left(self, event):
        self.circuit_solver_model.release_dragged_area()
        
    def __clicked_right(self, event):
        self.circuit_solver_model.update_position(event.x, event.y)
        self.circuit_solver_model.update_dragged_position(event.x, event.y)
        self.circuit_solver_model.handle_start_connecting()

    def __moved_right(self, event):
        self.circuit_solver_model.update_position(event.x, event.y)

    def __released_right(self, event):
        self.circuit_solver_model.update_position(event.x, event.y)
        self.circuit_solver_model.handle_stop_connecting()

    def render(self):
        self.canvas.delete("all")
        self.circuit_solver_model.render(self.canvas)
        self.canvas.pack()
        self.root.after(10, self.render)
