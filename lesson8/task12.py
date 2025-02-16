def gcd(first_num, second_num):
    while True:
        if first_num > second_num:
            second_num, first_num = first_num, second_num
        elif second_num - first_num == 0:
            return f"gcd is {first_num}"
        else:
            second_num = second_num - first_num

first = int(input("Enter the first num: "))
second = int(input("Enter the second num: "))
print(gcd(first, second))

