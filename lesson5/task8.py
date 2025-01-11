nums = range(10, 100)
for num in nums:
    num1 = num % 10
    num2 = num // 10
    num3 = (num1 * num2) * 3
    if num == num3:
        print(num)
