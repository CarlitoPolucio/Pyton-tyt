
secret = int(input("num: "))

num = 0
count = 0

if secret >= 50:
    count += 1
    if secret >= 75:
        count += 1
        if secret >= 88:
            count += 1
            num = 88
            while num != secret:
                count += 1
                num += 1
        else:
            count += 1
            while num != secret:
                count += 1
                num += 1
    elif secret < 75:
        count += 1
        num = 64
        if secret <= 63:
            num = 50
            count += 1
            while num != secret:
                count += 1
                num += 1
        else:
            count += 1
            while num != secret:
                count += 1
                num += 1

if secret < 50:
    count += 1
    if secret <= 25:
        count += 1
        while num != secret:
            count += 1
            num += 1
    else:
        count += 1
        num = 26
        while num != secret:
            count += 1
            num += 1


print(count)





