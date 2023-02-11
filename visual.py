import tkinter as tk

from gates import *


class SimulationWindow:
    def __init__(self, wires, gates):
        self.gates = gates
        self.wires = wires
        self.win = tk.Toplevel()
        self.frame = tk.Frame(self.win)
        self.canvas = tk.Canvas(self.frame, height=200, width=200, background="black")
        self.canvas.pack(fill=tk.BOTH, expand = 1)
        self.win.grab_set()

        self.draw()

        self.win.mainloop()

    def draw(self):
        print(self.gates)
        for x in range(0, len(self.gates)):
            for y in range(0, len(self.gates[x])):
                print(self.gates[x][y].gate)
                self.gates[x][y].gate.draw(x, y, self.canvas)
        self.canvas.update()
