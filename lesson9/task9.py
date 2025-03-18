def bin_search(array, need_to_find):
    if not need_to_find in array:
        return
    max_index = len(array) - 1
    min_index = 0
    count = 0
    while array[max_index] != need_to_find != array[min_index]:
        count += 1
        if need_to_find in array[(min_index + max_index) // 2:]:
            min_index = (min_index + max_index) // 2
        elif need_to_find in array[:(max_index + min_index) // 2]:
            max_index = (max_index + min_index) // 2
    return array.index(need_to_find), count


user_massive = list(range(1, 1000000, 7))
find_value = 623057
print(bin_search(user_massive, find_value))
