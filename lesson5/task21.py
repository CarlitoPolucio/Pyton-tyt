y = int(input("Enter girls: "))
x = int(input("Enter boys: "))

if x / y > 2 or y / x > 2:
    print("unreal")
    exit()

if y == x:
    while y > 0:
        x -= 1
        y -= 1
        print("BG",end="")
    else:
        exit()

if y > x:
    print("G", end="")
    y -= 1
    print("B", end="")
    x -= 1
else:
    print("B", end="")
    x -= 1
    print("G", end="")
    y -= 1

if y > x:
    while y > 1:
        y -= 1
        print("G",end="")
        y -= 1
        print("G",end="")
        x -= 1
        print("B",end="")
    if x > y:
        x -= 1
        print("B",end="")
    elif y == x:
        print("GB",end="")
    else:
        y -= 1
        print("G",end="")


if x > y:
    while x > 1:
        x -= 1
        print("B",end="")
        x -= 1
        print("B",end="")
        y -= 1
        print("G",end="")
    if y > x:
        y -= 1
        print("G",end="")
    elif y == x:
        print("BG",end="")
    else:
        x -= 1
        print("B",end="")









