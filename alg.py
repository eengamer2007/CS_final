import sys
from gates import *
from dataclasses import dataclass
from random import randint

@dataclass
class LocalGate:
    type: GateType
    connections: tuple[list[(int)], list[(int)]]

def run(inputs: int, gate1: int, gate2: int, output: int = 1) -> dict | str:
    if output > 1:
        return "too many outputs"
    if inputs > 1 + gate2:
        return "not enough gates or too many inputs"
    gen_layout(inputs, gate2, output)
    return {}


def gen_layout(inputs: int, gates: int, outputs: int) -> dict:
    layers: list = []
    layers.append([])
    
    # show open spots (layer, index)
    open: list[(int, int)] = []

    # add outputs to layer 0
    for i in range(outputs):
        layers[0].append(GateType.OUTPUT)
        open.append((0, i))

    while len(open) < inputs:
        index = randint(0, len(open) - 1)
        print(open[index])
        if len(layers) < open[index][0]:
           layers.append([])
        location = open.pop(index)
        
        



# set the types of the gates
def fill_gates():
    pass

# generate the logic table
def gen_table():
    pass


if __name__ == "__main__":
    out = run(2, 1, 2)
    if type(out) == dict:
        print("output", out)
    else:
        print("something wrong: " + out, file=sys.stderr)
