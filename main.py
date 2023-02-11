# /usr/bin/python3

import tkinter as tk

from gates import *
from alg import *


class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)
        self.grid = self.frame.grid()

        self.menu()

        tk.mainloop()

    def menu(self):
        gate1 = tk.Label(text="gate 1")
        gate1.grid(column=1, row=0)

        self.gate1list = tk.Variable(value=gate1_list)

        self.gate1listbox = tk.Listbox(listvariable=self.gate1list)
        self.gate1listbox.grid(column=1, row=1, columns=3)

        gate2 = tk.Label(text="gate 2")
        gate2.grid(column=2, row=0)

        self.gate2list = tk.Variable(value=gate2_list)

        self.gate2listbox = tk.Listbox(listvariable=self.gate2list)
        self.gate2listbox.grid(column=2, row=1, columns=3)


if __name__ == '__main__':
    win = Window()
