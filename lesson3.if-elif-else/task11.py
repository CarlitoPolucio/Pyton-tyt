num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
num3 = int(input("Enter the number: "))

if num2 < num1 > num3:
    print(num1)
elif num3 < num2 > num1:
    print(num2)
else:
    print(num3)

# Оптимизация

# num1 = int(input("Enter the number: "))
# num2 = int(input("Enter the number: "))
# num3 = int(input("Enter the number: "))
#
#
# if num1 > num2:
#     max_num = num1
# else:
#     max_num = num2
#
# if num3 > max_num:
#     max_num = num3
#
# print(max_num)
