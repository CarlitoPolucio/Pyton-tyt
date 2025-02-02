matrice = int(input("Enter the size of matrice: "))

for num in range(1, matrice + 1):
    for num1 in range(1, matrice + 1):
        if num1 % 3 == 0:
            print(num1, "\t", end="")
        else:
            print(num, "\t", end="")
    print()