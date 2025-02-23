def amp(a, b):
    counter = 0
    while a >= b:
        a = a - a * 0.084
        counter += 1
    return counter


start = float(input("Enter start val: "))
stop = float(input("Enter stop val: "))
print(amp(start,stop))


