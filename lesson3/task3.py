number = int(input("Введите число: "))
check = (number // 2)
if number / 2 > check:
    print("Number is not even")
else:
    print("Number is even")

# Оптимизация:
# number = int(input("Введите число: "))
#
# if number % 2 != 0:
#     print("Number is not even")
# else:
#     print("Number is even")