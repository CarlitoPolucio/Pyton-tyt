user_input = int(input("enter the height: "))

mid = user_input * 2
amount_numbers = 0
counter = 0
numbers = 1

for num1 in range(1, user_input + 1):
    amount_numbers += 1
    counter = 0
    mid -= 2
    print(" " * mid, end="")
    while counter != amount_numbers:
        counter += 1
        print(numbers, " ", end="")
        numbers += 2

    print()


