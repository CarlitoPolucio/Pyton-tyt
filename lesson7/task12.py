user_input = int(input("Enter the num: "))

count = 0

for num in range(1, user_input + 1):
    value = str(num) + str(num) * count
    print(" ".join(value))
    count += 1


