def sort(massive):
    max_num = massive.index(max(massive))
    min_num = massive.index(min(massive))
    massive[min_num], massive[max_num] = massive[max_num], massive[min_num]
    return massive


us_list = [23, 2344, 4545, 232325, 234]
print(sort(us_list))