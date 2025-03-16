a = [1, 3, 4 , 1, -2, 3]
pivot = a[0]

less = [i for i in a[1:] if i > pivot]

print(less)