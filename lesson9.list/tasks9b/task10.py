def semen_lists(a, b, c):
    a += b
    print(a.count(5))
    [a.remove(x) for x in a if x == 5]
    a += c
    print(a.count(3), "\n", a)


one = [1, 5, 3]
two = [1, 5, 1, 5]
three = [1, 3, 1, 5, 3, 3]
semen_lists(one, two, three)