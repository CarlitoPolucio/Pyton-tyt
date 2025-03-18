def list_sort(array):
    change = True
    while change:
        change = False
        for i, num in enumerate(array):
            try:
                array[i + 1]
            except IndexError:
                continue
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                change = True
    return array


user_array = [-5, 3, 8, 2, 12, 9, -2, 1, 1]
print(list_sort(user_array))


