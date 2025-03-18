def max_num_search(massive):
    max_num = 0
    for num in test_list:
        if num > max_num:
            max_num = num
    return max_num


test_list = [1, 20, 456, 2345, 123, 22, 324244]

print(max_num_search(test_list))

