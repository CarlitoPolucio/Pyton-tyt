def lists_sort(a, b):
   return sorted(a + [y for y in b if not y in a])


first = [1, 2, 5, 20]
second = [2, 20, 30, 40, 3, 1]
print(lists_sort(first,second))


