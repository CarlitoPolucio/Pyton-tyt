value = int(input("enter the last num: "))
nums = range(2, value + 1, 2)

for num in nums:
    num **= 3
    print(num)
