import random

first = [random.randint(50, 80) for x in range(1, 11)]
second = [random.randint(30, 60) for y in range(1, 11)]
fight = ["died" if random.choice(first) + random.choice(second) > 100 else "survived" for x in range(1, 11)]

print(first, "\n", second, "\n", fight)