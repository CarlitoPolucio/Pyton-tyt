a = [1, 2, 2, 2, 1, 1]
to_add = []
if a[0] != a[-1]:
    to_add.append(a[0])
for i, num in enumerate(a[:-1]):
    if num == a[-i -2]:
        to_add.append(num)


print(to_add, len(to_add))