import math

def diff(x):
    answer = (4/3 * math.pi) * x ** 3 / (1.08321 * 10 ** 12)
    return round(answer, 3)


user_input = float(input("Enter radius: "))
print(diff(user_input))

