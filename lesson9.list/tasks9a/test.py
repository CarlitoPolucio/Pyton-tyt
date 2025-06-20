import math


def bin_search(array, need_to_find):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2  # Целочисленное деление
        if array[mid] == need_to_find:
            return mid  # Возвращаем индекс найденного элемента
        elif array[mid] < need_to_find:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Элемент не найден


user_massive = list(range(-10000, 10000, 3))
find_value = -2908
print(bin_search(user_massive, find_value))
