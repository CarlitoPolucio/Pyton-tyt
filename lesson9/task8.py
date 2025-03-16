def СДВИГ(massive, step):
    step %= len(massive)
    output = massive[-step:] + massive[:-step]
    print(output)


step = 3
user_list = [1, 4, -3, 0, 10]
print(СДВИГ(user_list, step))
