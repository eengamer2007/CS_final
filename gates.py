import tkinter as tk
from dataclasses import dataclass
from enum import Enum
from typing import Callable

SPACING_GATE = 20
SPACING_WIRE = 5
SIZE_GATE = 20

class GateType(Enum):
    GATE1 = "gate1",
    GATE2 = "gate2",
    INPUT = "input",
    OUTPUT = "output",

    def __repr__(self) -> str:
        return self.value[0]

    def __str__(self) -> str:
        return self.value[0]


@dataclass
class Gate:
    type: GateType
    name: str
    inputs: int
    fn: Callable
    draw: Callable
    wirecon: tuple[list[(int, int)], list[(int, int)]]

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name


def draw_fn(x, y, canvas: tk.Canvas):
    #print("drawing")
    canvas.create_rectangle((x, y), (x + 20, y + 20))


gate1_list = [
    Gate(type=GateType.GATE1, name="not", inputs=1,
         fn=lambda x: not x, draw=draw_fn, wirecon=([(0, 5)], [(10, 5)]))
]

gate2_list = [
    Gate(type=GateType.GATE2, name="and", inputs=2,
         fn=lambda x, y: x and y, draw=draw_fn, wirecon=([(0, 2), (0, 8)], [(10, 5)])),
    Gate(type=GateType.GATE2, name="or", inputs=2,
         fn=lambda x, y: x or y, draw=draw_fn, wirecon=([(0, 2), (0, 8)], [(10, 5)])),
    Gate(type=GateType.GATE2, name="xor", inputs=2,
         fn=lambda x, y: x != y, draw=draw_fn, wirecon=([(0, 2), (0, 8)], [(10, 5)]))
]


def draw_input(x, y, canvas):
    draw_fn(x, y, canvas)
    canvas.create_oval((x + 2, y + 2), (x + 18, y + 18), fill="yellow")


def draw_output(x, y, canvas):
    draw_fn(x, y, canvas)
    canvas.create_oval((x + 2, y + 2), (x + 18, y + 18), fill="red")


output_gate = Gate(type=GateType.OUTPUT, name="output",
                   inputs=1, fn=lambda x: ..., draw=draw_output, wirecon=([(0, 5)], []))
input_gate = Gate(type=GateType.OUTPUT, name="output",
                  inputs=0, fn=lambda: ..., draw=draw_input, wirecon=([], [(10, 5)]))
