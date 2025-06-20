import random

random_list = [random.randint(0, 100) for num in range(10)]
answer = [tuple(random_list[i: i + 2]) for i in range(0, 10, 2)]
print(random_list)
print(answer)