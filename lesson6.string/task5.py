first_num = int(input("Enter num: "))
step = int(input("Enter step: "))

last_num = 0

for num in range(first_num, first_num + step * 3, step):
    last_num += num
    print(num, ".", sep="", end="")
print(last_num)
