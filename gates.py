from dataclasses import dataclass
from typing import Callable

@dataclass
class Gate:
    name: str
    inputs: int
    fn: Callable
    
    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name

gate1_list = [
    Gate( name = "not", inputs = 1, fn = lambda x: not x)
]

gate2_list = [
    Gate(name = "and", inputs = 2, fn = lambda x,y: x and y),
    Gate(name = "or",  inputs = 2, fn = lambda x,y: x or y ),
    Gate(name = "xor", inputs = 2, fn = lambda x,y: x != y )
]
