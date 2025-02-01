width = int(input("Enter the width: "))

for sign in range(1, width + 1):
    print("-", end="")

for sign2 in range(1, width + 1):
    print("")
    for sign in range(1, width + 1):
        if sign == 1 or sign == width:
            print("|", end="")
        else:
            print(" ", end="")