user_input = int(input("enter the height: "))

mid = user_input - 1
jail = 1

for num1 in range(1, user_input + 1):
    print(" " * mid, "#" * jail)
    mid -= 1
    jail += 2

