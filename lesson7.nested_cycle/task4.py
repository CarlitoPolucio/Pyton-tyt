width = int(input("Enter the width: "))
height = int(input("Enter the height: "))

for num in range(1, height + 1):
    if num % 2 == 0:
       for num1 in range(1, width + 1):
           print(num, "\t", end="")
    if num % 2 > 0:
        for num2 in range(1, width + 1):
            print(num2, "\t", end="")
    print("")

