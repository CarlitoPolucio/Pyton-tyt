first_num = int(input("Enter the first num: "))
last_num = int(input("Enter the last num: "))
step = int(input("Enter the step: "))

if first_num > last_num:
    first_num, last_num = last_num, first_num
if step > 0:
    step //= -1

user_range = range(last_num, first_num -1, step)

for x in user_range:
    y = (x ** 3 + 2 * x ** 2) - 4 * x + 1
    print(y)


