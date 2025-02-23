from math import sqrt


def find_p(a, b, c):
    return (a + b + c) / 2


def find_s(p, a, b, c):
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    return s


first = int(input("Enter a: "))
second = int(input("Enter b: "))
third = int(input("Enter b: "))

p = find_p(first, second, third)
print(find_s(p, first, second, third))
