first_num = 0
step = 1
last_num = 9

for num in range(first_num, last_num, step):
    first_num += 1
    step = first_num
    last_num = first_num * 9
    for num1 in range(first_num, last_num + 1, step):
            print(num1, "\t", end="")
            if num1 == last_num:
                print("")
