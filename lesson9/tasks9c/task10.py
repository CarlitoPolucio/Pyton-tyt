import random

first = [round(random.uniform(5, 10), 2) for x in range(21)]
second = [round(random.uniform(5, 10), 2) for y in range(21)]
comp = [x if x > second[i] else second[i] for i, x in enumerate(first)]
print(first, "\n", second, "\n", comp)