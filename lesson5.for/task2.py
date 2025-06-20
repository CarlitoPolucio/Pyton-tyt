nums = 345, 19, 87, 1020, 421, 925, 5
count = 0
for num in nums:
    if 10 > (num // 100) > 0 and (num % 5) == 0:
        count += 1
        print(f"win:{num}.")
print(f"We've got {count} winners")
