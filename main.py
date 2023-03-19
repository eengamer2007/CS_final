#!/usr/bin/python3

from tkinter import messagebox

import visual
from alg import *
from gates import *


class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)
        self.frame.grid()

        self.menu()

        tk.mainloop()

    def menu(self):
        gate1 = tk.Label(text="gate 1")
        gate1.grid(column=1, row=0)

        # start button
        self.s_button = tk.Button(text="start", command=self.run)
        self.s_button.grid(column=0, row=3)

        # select amount gate 1
        tk.Label(text="gate 1 amount").grid(column=0, row=0)
        self.gate1amount = tk.Entry()
        self.gate1amount.grid(column=1, row=0)

        # select amount gate 2
        tk.Label(text="gate 2 amount").grid(column=0, row=1)
        self.gate2amount = tk.Entry()
        self.gate2amount.grid(column=1, row=1)

        # select amount input
        tk.Label(text="input amount").grid(column=0, row=2)
        self.inputamount = tk.Entry()
        self.inputamount.grid(column=1, row=2)

        # show list gate 1
        gate2 = tk.Label(text="gate 1")
        gate2.grid(column=2, row=0)
        self.gate1list = tk.Variable(value=gate1_list)

        self.gate1listbox = tk.Listbox(listvariable=self.gate1list)
        self.gate1listbox.grid(column=2, row=1, rows=3)

        # show list gate 2
        gate2 = tk.Label(text="gate 2")
        gate2.grid(column=3, row=0)

        self.gate2list = tk.Variable(value=gate2_list)

        self.gate2listbox = tk.Listbox(listvariable=self.gate2list)
        self.gate2listbox.grid(column=3, row=1, rows=3)

    def run(self):
        try:
            gate1_count = int(self.gate1amount.get())
            gate2_count = int(self.gate2amount.get())
            input_count = int(self.inputamount.get())
        except ValueError:
            messagebox.showerror(
                "invalid value", "an invalid number was entered into the inputs")
            return

        try:
            res = run(input_count, gate1_count, gate2_count)
        except ValueError as x:
            messagebox.showerror("run error", x)
            return

        visual.SimulationWindow(res[0], res[1])


if __name__ == '__main__':
    win = Window()
