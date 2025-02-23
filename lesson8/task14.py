def maximum_of_two(a, b):
    if a > b:
        return a
    else:
        return b


def maximum_of_three(a, b, c):
    if c > maximum_of_two(a, b):
        return c
    else:
        return maximum_of_two(a, b)


first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))

print(maximum_of_three(first, second, third))
