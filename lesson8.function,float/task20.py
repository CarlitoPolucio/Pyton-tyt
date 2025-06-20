a = 1
count = 0
while a > 0:
    if a / 2 == 0:
        count += 1
        break
    a /= 2
    count += 1
print(count, a)
