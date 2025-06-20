numbers = [4, 5, 3, 4, 5, 6, 7, 8, 9, 10]
a = 3
b = 6
print([num for i, num in enumerate(numbers) if i not in range(a, b + 1)])
