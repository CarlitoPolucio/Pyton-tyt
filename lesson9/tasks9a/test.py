import math


def bin_search(array, need_to_find):
    max_index = len(array) - 1
    min_index = 0
    if array[max_index] == need_to_find:
        return array[max_index]
    elif array[min_index] == need_to_find:
        return array[min_index]
    else:
        while max_index - min_index != 1:
            average = math.ceil((min_index + max_index) / 2)
            if need_to_find > array[average]:
                min_index = average
            elif need_to_find < array[average]:
                max_index = average
            else:
                return array[average], average
        return


user_massive = list(range(-10000, 10000, 3))
find_value = -1
print(bin_search(user_massive, find_value))
