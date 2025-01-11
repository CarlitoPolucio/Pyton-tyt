numbers = range(10, 100)
ten = range(0, 10)

for num in str(numbers):
    count = 1
    count *= int(num)
    print(count)
    if num % 3 == 0:

        print(num)