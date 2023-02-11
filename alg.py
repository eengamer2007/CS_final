import sys
import gates
from dataclasses import dataclass
from random import randint, choice


@dataclass
class LocalGate:
    type: gates.GateType
    # first input second output
    connections: tuple[list[(int, int)], list[(int, int)]]


@dataclass
class OutGate:
    gate: gates.Gate
    # first input second output
    connections: tuple[list[(int, int)], list[(int, int)]]


def run(inputs: int, gate1: int, gate2: int, gate1_list=gates.gate1_list, gate2_list=gates.gate2_list, output: int = 1) -> dict:
    if output > 1:
        raise ValueError("too many outputs")
    if inputs > output + gate2:
        raise ValueError("mismatch between inputs and gate2")

    layout = gen_layout(inputs, gate2, output)

    extra_added = add_extra(layout[0], layout[1])

    gates_filled = fill_gates(extra_added[1])

    return (extra_added[0], gates_filled)


def gen_layout(inputs: int, gate: int, outputs: int) -> tuple[list, list]:
    layers: list = []
    layers.append([])

    wires: list[((int, int)(int, int))] = []

    # show open spots (layer, index)
    open: list[(int, int)] = []

    # add outputs to layer 0
    for i in range(outputs):
        layers[0].append(LocalGate(type=gates.GateType.OUTPUT, connections=([], [])))
        open.append((0, i))

    print("open:", open)

    for i in range(len(layers)):
        print(i, ":", layers[i])
    print()

    while len(open) < inputs:
        # choose random open
        index = randint(0, len(open) - 1)
        print(index)
        loc = open.pop(index)

        print(loc)

        # check if the layer the new port is on exist and if not make it
        if len(layers) < loc[0] + 2:
            layers.append([])

        # pop the open port from the list

        layers[loc[0] + 1].append(
            LocalGate(
                type=gates.GateType.GATE2,
                connections=([], [loc])
            )
        )

        new_loc: tuple[int, int] = (loc[0]+1, len(layers[loc[0] + 1]) - 1)

        wires.append((loc, new_loc))

        layers[loc[0]][loc[1]].connections[0].append(new_loc)

        open.append(new_loc)
        open.append(new_loc)

        print(open)
        print("layers:", len(layers))
        for i in range(len(layers)):
            print(i, ":", layers[i])
        print("wires:", wires)
        print()
    return (wires, layers)

# add extra ports


def add_extra(wires, layout):
    return (wires, layout)

# set the types of the gates


def fill_gates(layout):
    print(layout)
    print("call fill gates")
    out = []
    for x in range(0, len(layout) - 1):
        print(x)
        print("l",len(layout[x]))
        out.append([])
        for y in range(0, len(layout[x])):
            print(" ",y)
            out[x].append("thing")
            print(layout[x][y])
            match layout[x][y].type:
                case gates.GateType.GATE1:
                    print("gate 1")
                    out[x][y] = OutGate(gate=choice(gates.gate1_list),
                                connections=layout[x][y].connections)
                case gates.GateType.GATE2:
                    print("gate2")
                    out[x][y] = OutGate(gate=choice(gates.gate2_list),
                                connections=layout[x][y].connections)
                case gates.GateType.INPUT:
                    print("input")
                    out[x][y] = OutGate(gate=gates.input_gate, connections=layout[x][y].connections)
                case gates.GateType.OUTPUT:
                    print("output")
                    out[x][y] = OutGate(gate=gates.output_gate, connections=layout[x][y].connections)
    print(out)
    return out


# generate the logic table
def gen_table():
    pass


if __name__ == "__main__":
    out = run(10, 0, 9)
    print("output:", out)
