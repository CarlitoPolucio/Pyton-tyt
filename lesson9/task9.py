from math import log2, ceil


def bin_search(array, need_to_find):
    max_index = max(array)
    min_index = min(array)
    count = 0
    while max_index != need_to_find != min_index:
        count += 1
        if need_to_find in array[(max_index + min_index) // 2:]:
            min_index = (max_index + min_index) // 2
        elif need_to_find in array[min_index:max_index]:
            max_index = (max_index + min_index) // 2
        if count > ceil(log2(max(array) - min(array) - 1)):
            return
    return array.index(find_value), count


user_massive = list(range(1, 1000001))
find_value = 465
print(bin_search(user_massive, find_value))
