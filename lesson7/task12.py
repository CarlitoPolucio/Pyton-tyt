user_input = int(input("Enter the num: "))

step = 2

for num in range(1, user_input + 1):
    for num1 in range(num, step + 1):
        print(str(num1) * step)
        step += 1
    print(" ")