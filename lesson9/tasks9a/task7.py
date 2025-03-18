def include(massive, new_num):
    massive.append(new_num)
    massive.sort()
    massive.reverse()
    return massive


nums = [5, 4, 3, 3, 2, 1]
num_to_include = 4
print(include(nums, num_to_include))