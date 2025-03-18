def bin_search(array, need_to_find):
    if not need_to_find in array:
        return
    max_index = len(array) - 1
    min_index = 0
    count = 0
    while max_index - min_index != 2 :
        count += 1
        if need_to_find > array[(min_index + max_index) // 2]:
            min_index = (min_index + max_index) // 2
        elif need_to_find < array[(max_index + min_index) // 2]:
            max_index = (max_index + min_index) // 2
    return array[max_index - 1] if array[max_index - 1] == need_to_find else None


user_massive = list(range(100))
find_value = 50
print(bin_search(user_massive, find_value))
