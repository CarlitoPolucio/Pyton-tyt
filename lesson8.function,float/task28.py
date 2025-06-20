from math import log, exp, ceil, floor


def poz(user_num):
    return log(ceil(user_num))


def neg(user_num):
    return exp(floor(user_num))


while True:
    user_input = float(input("Enter the num: "))
    if user_input > 0:
        print(poz(user_input))
    elif user_input < 0:
        print(neg(user_input))
    else:
        print("0")
