from gates import *

SPACING_GATE = 20
SPACING_WIRE = 5
SIZE_GATE = 20


class SimulationWindow:
    def __init__(self, wires, gates):
        self.gates = gates
        self.wires = wires
        self.win = tk.Toplevel()
        self.win.grab_set()
        self.canvas: tk.Canvas = tk.Canvas(self.win, height=200, width=200)
        self.draw()
        self.canvas.place(relheight=1, relwidth=1, x=0, y=0)

        self.win.mainloop()

    def draw(self):
        print("\n" + str(self.gates))
        print()
        for x_gate, i in enumerate(self.gates):  # range(0, len(self.gates))
            for y_gate, j in enumerate(i):
                print(j.gate, x_gate, y_gate)
                j.gate.draw(y_gate * (SIZE_GATE + SPACING_GATE) + SPACING_GATE,
                            x_gate * (SIZE_GATE + SPACING_GATE) + SPACING_GATE, self.canvas)
                for wires in j.connections:
                    print("conn:" + str(wire))
                    for wire in wires:
                        ...
        self.canvas.update()
