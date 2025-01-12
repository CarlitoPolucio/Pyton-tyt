y = int(input("Enter girls: "))
x = int(input("Enter boys: "))

girls_list = range(0, y)
boys_list = range(0, x)

if y > x:
    print("G", end="")
    y -= 1
else:
    print("B", end="")
    x -= 1




if y > x:
    while y != 0:
        if y / x > 1.9:
            y -= 2
            print("GG", end="")
        else:
            x -= 1
            print("B", end="")
        if x / y > 1.9:
            x -= 2
            print("BB", end="")
        elif y >= 2:
            y -= 2
            print("GG", end="")
        else:
            y -= 1
            print("G", end="")
if x > y:
    while x != 0:
        if x / y > 1.9:
            x -= 2
            print("BB", end="")
        else:
            y -= 1
            print("G", end="")
        if x >= 2:
            x -= 2
            print("BB", end="")
        else:
            x -= 1
            print("B", end="")



