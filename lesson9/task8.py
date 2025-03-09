def СДВИГ(massive, step):
    output = [massive.index(num + step) for num in massive]
    return massive


step = 3
user_list = [1, 4, -3, 0, 10]
print(СДВИГ(user_list,step))

