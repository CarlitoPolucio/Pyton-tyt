value = int(input("enter the last num: "))

counter = 0

nums = range(0, value + 1, 5)
for num in nums:
    counter += num
print(counter)
