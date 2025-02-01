w = 8
a = 10

while True:
    command = input("Enter the command: ")
    if command == "a" and a > 0:
        a -= 1
    elif command == "d" and a < 20:
        a += 1
    elif command == "w" and w < 15:
        w += 1
    elif command == "s" and w > 0:
        w -= 1
    else:
        print("no more")
    print(f"position is {a}, {w}")



