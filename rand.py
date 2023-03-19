import math


def pop_random(list: list):
    num = random(len(list))
    print("num:", num)
    num *= len(list) - 1
    num = math.floor(num)
    print("pop: " + str(num) + "from array len: " + str(len(list)))
    return list.pop(num)


# returns a float between
def random(size: int) -> float:
    used_bytes = math.ceil(
        math.log2(
            size
        ) / 8
    )
    print("bytes:", used_bytes)
    with open("/dev/urandom", "rb") as handle:
        num = handle.read(used_bytes)
    print("raw:", num)
    num = int.from_bytes(num, "big")
    print("num:", num)
    print("max:", pow(2, used_bytes*8))
    num /= pow(2, used_bytes*8)
    return num


if __name__ == "__main__":
    print("testing rand lib")
    for i in range(10):
        print("res:", random(100))
