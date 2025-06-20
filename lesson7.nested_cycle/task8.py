numbers = int(input("Enter the amount of numbers: "))

common_num_counter = 0
counter = 0

for num in range(1, numbers + 1):
    common_num_counter += counter
    num1 = int(input("enter the num1: "))
    num2 = int(input("enter the num2: "))
    if num1 == 1:
        num1 += 1
    counter = num2 - num1 + 1
    for num3 in range(num1, num2 + 1):
        radical = (num2 ** 0.5) // 1
        for rad in range(2, int(radical) + 1):
            if num3 == rad:
                continue
            if num3 % rad == 0:
                counter -= 1
                break

common_num_counter += counter

print(common_num_counter)



