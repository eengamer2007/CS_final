import math


def pop_random(list: list):
    num = random(len(list))
    num *= len(list)
    num = math.floor(num)
    list.pop(num)

    return


# returns a float between
def random(size: int) -> float:
    with open("/dev/urandom", "rb") as handle:
        num = handle.read(math.ceil(math.log2(size)))

    num = int.from_bytes(num, "big")
    num /= pow(2, math.ceil(math.log2(size)))
    return num
