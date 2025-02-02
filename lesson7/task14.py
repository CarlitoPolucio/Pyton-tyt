user_input = int(input("Enter the num: "))

iteration = user_input

for num in range(0, user_input + 1):
    for num1 in range(num, -iteration - 1, -1):
        print(num1, "\t", end="")
    iteration -= 1
    print()