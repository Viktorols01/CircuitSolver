import tkinter as tk
from tkinter import messagebox

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

        top_bar = tk.Frame(self.root, height=40)
        top_bar.pack(side="top", fill="x")

        options = ["Resistance", "Source", "Diode"]
        selected = tk.StringVar(value=options[0])
        dropdown = tk.OptionMenu(top_bar, selected, *options)
        dropdown.pack(side="left")

        def add_component():
            match selected.get():
                case "Source":
                    self.circuit_solver_model.add_twopole(GSource(20, 20))
                case "Resistance":
                    self.circuit_solver_model.add_twopole(GResistance(20, 20))
                case "Diode":
                    self.circuit_solver_model.add_twopole(GDiode(20, 20))
        add_button = tk.Button(top_bar, text="Add", command=add_component)
        add_button.pack(side="left")

        def show_help():
            tk.messagebox.showinfo("Info", "Use left click to drag nodes and twopoles. Use right click to connect sockets.")
        help_button = tk.Button(top_bar, text="?", command=show_help)
        help_button.pack(side="right")

        def solve():
            success = self.circuit_solver_model.solve()
            if not success:
                tk.messagebox.showinfo("Error", "CircuitSolver did not succeed in solving the provided system.")
                
        solve_button = tk.Button(top_bar, text="Solve", command=solve)
        solve_button.pack(side="left")

        self.width = width
        self.height = height
        self.canvas = tk.Canvas(self.root, background="darkgray", width=width, height=height)
        self.canvas.pack()

        self.canvas.bind("<Motion>", self._motion)
        self.canvas.bind("<Button-1>", self._clicked_left)
        self.canvas.bind("<B1-Motion>", self._moved_left)
        self.canvas.bind("<ButtonRelease-1>", self._released_left)
        self.canvas.bind("<Button-3>", self._clicked_right)
        self.canvas.bind("<B3-Motion>", self._moved_right)
        self.canvas.bind("<ButtonRelease-3>", self._released_right)

        self.root.after(10, self.render)
        self.root.mainloop()

    def _motion(self, event):
        self.circuit_solver_model.update_position(event.x, event.y)

    def _clicked_left(self, event):
        self.circuit_solver_model.update_position(event.x, event.y)
        self.circuit_solver_model.update_dragged_position(event.x, event.y)
        self.circuit_solver_model.pickup_dragged_area()

    def _moved_left(self, event):
        self.circuit_solver_model.update_position(event.x, event.y)
        self.circuit_solver_model.move_dragged_area()

    def _released_left(self, event):
        self.circuit_solver_model.release_dragged_area()
        
    def _clicked_right(self, event):
        self.circuit_solver_model.update_position(event.x, event.y)
        self.circuit_solver_model.update_dragged_position(event.x, event.y)
        self.circuit_solver_model.handle_start_connecting()

    def _moved_right(self, event):
        self.circuit_solver_model.update_position(event.x, event.y)

    def _released_right(self, event):
        self.circuit_solver_model.update_position(event.x, event.y)
        self.circuit_solver_model.handle_stop_connecting()

    def render(self):
        self.canvas.delete("all")
        self._render_background(self.canvas)
        self.circuit_solver_model.render(self.canvas)
        self.canvas.pack()
        self.root.after(10, self.render)

    def _render_background(self, canvas):
        s = 20
        for x in range(s//2, self.width, s):
            for y in range(s//2, self.height, s):
                r = 1
                canvas.create_oval(x, y, x + r, y + r, outline="lightgray")