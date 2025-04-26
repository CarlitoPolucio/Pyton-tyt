def ten(num):
    if num == 1:
        return print(num)
    else:
        ten(num - 1)
        return print(num)


ten(10)