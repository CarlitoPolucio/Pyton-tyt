import math


def format_num(num):
    if x < 1:
        return f"x = {x * 10 ** (str(x).count("0"))} * {10} ** -{str(x).count("0")}"
    return f"x = {x / 10 ** (len(str(math.trunc(x))) - 1)} * {10} ** {(len(str(math.trunc(x))) - 1)}"


x = 92345
print(format_num(x))
