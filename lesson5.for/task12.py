value = int(input("enter the last num: "))
nums = range(1, value + 1, 2)
for num in nums:
    num **= 2
    print(num)
