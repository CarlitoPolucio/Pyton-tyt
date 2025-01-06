last = int(input("Enter the last number: "))
num = 1
num1 = 1
while num <= last:
    num1 = num1 ** 3
    print(num1)
    num += 1
    num1 = num
