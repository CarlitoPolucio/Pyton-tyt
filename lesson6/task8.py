w = 8
s = w
a = 10
d = a


while True:
    command = input("Enter the command: ")
    if command == "a" and a > 0:
        a -= 1
    elif command == "d" and d < 20:
        d = a
        d += 1
    elif command == "w" and w < 15:
        w += 1
    elif command == "s" and s > 0:
        s = w
        s -= 1
    else:
        print("no more")
    print(f"position is {a}, {w}")



