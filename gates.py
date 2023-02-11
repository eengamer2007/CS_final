from dataclasses import dataclass
from typing import Callable
from enum import Enum

class GateType(Enum):
    GATE1 = "gate1",
    GATE2 = "gate2",
    INPUT = "input",
    OUTPUT = "output",

@dataclass
class Gate:
    type: GateType
    name: str
    inputs: int
    fn: Callable

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name


gate1_list = [
    Gate(type=GateType.GATE1, name="not", inputs=1, fn=lambda x: not x)
]

gate2_list = [
    Gate(type=GateType.GATE2, name="and", inputs=2, fn=lambda x, y: x and y),
    Gate(type=GateType.GATE2, name="or",  inputs=2, fn=lambda x, y: x or y),
    Gate(type=GateType.GATE2, name="xor", inputs=2, fn=lambda x, y: x != y)
]
