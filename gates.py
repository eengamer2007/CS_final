from dataclasses import dataclass
from typing import Callable
from enum import Enum

import tkinter as tk


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

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name

def draw_fn(x,y,canvas: tk.Canvas):
    print("drawing")
    canvas.create_rectangle((x,y), (x+100, y+100), fill="black")

gate1_list = [
    Gate(type=GateType.GATE1, name="not", inputs=1,
         fn=lambda x: not x, draw=draw_fn)
]

gate2_list = [
    Gate(type=GateType.GATE2, name="and", inputs=2,
         fn=lambda x, y: x and y, draw=draw_fn),
    Gate(type=GateType.GATE2, name="or",  inputs=2,
         fn=lambda x, y: x or y, draw=draw_fn),
    Gate(type=GateType.GATE2, name="xor", inputs=2,
         fn=lambda x, y: x != y, draw=draw_fn)
]

output_gate = Gate(type=GateType.OUTPUT, name="output",
                   inputs=1, fn=lambda x: ..., draw=draw_fn)
input_gate = Gate(type=GateType.OUTPUT, name="output",
                  inputs=0, fn=lambda: ..., draw=draw_fn)
