num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))

sum_numbers = 0
count = 0

for numbers in range(num1, num2):
    if numbers % 3 == 0:
        sum_numbers += numbers
        count += 1

answer = sum_numbers / count
print(answer)
