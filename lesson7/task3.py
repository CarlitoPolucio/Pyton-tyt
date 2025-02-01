user_input = int(input("Enter the num: "))

for num in range(0, user_input + 1):
    for num1 in range(num, user_input + num + 1):
        print(num1, "", end="")
    print(" ")

