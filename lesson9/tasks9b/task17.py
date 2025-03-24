a = [1, 1, 2, 1, 1, 2]
a.reverse()
for i, x in enumerate(a[:-1]):
    if x != a[i + 1]:
        print(a[i + 1:], len(a[i + 1:]))
        break



