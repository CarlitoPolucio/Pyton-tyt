def del_big(massive):
     massive.remove(max(massive))
     return massive


list_num = [1, 9, 2, 4, 7, 4]
print(del_big(list_num))