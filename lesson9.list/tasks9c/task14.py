nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
print([x for z in [[x for y in z for x in y] for z in nice_list] for x in z])