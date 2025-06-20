import math


def format_num(num):
    if float(num) < 1:
        exponent = 1
        for symbol in num[2:]:
            if symbol == "0":
                exponent += 1
            else:
                break
        return f"x = {float(num) * 10 ** exponent} * {10} ** -{exponent}"
    return f"x = {float(num) / 10 ** (len(str(math.trunc(float(num)))) - 1)} * {10} ** {len(str(math.trunc(float(num)))) - 1}"


x = "43455"
print(format_num(x))
