import sys
from gates import *

def run(inputs: int, gate1: int, gate2: int, output: int = 1) -> dict | str:
    if output > 1:
        return "too many outputs"
    if inputs > 1 + gate2:
        return "not enough gates or too many inputs"
    gen_layout(inputs, gate2, output)
    return {}

def gen_layout(inputs: int, gates: int, outputs: int) -> dict:
    # dict has keys wich specify gate and the list is what connection and what gate
    output: dict[str, list[(str,(str, str))]] = dict()
    ins: list[str] = []
    outs: list[str] = []
    for i in range(gates):
        ins.append("g"+str(i))
    for i in range(gates):
        outs.append("g"+str(i)+".1")
        outs.append("g"+str(i)+".2")
    print(ins)
    print(outs)

def fill_gates():
    pass

def gen_table():
    pass

if __name__ == "__main__":
    out = run(2,1,2)
    if type(out) == dict:
        print(out)
    else:
        print("something wrong: " + out, file=sys.stderr)
