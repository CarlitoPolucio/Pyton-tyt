number = int(input("Ent num: "))

number = (number // 2) * 2

number_list = range(number, 1, -2)

for num in number_list:
    print(num)


