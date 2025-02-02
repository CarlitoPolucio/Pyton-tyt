user_input = int(input("Enter the num: "))

need_to_fill = user_input * 2 - 2
next_num = user_input
value = " "

for num1 in range(1, user_input + 1):
    next_num -= 1
    value += str(next_num)
    answer = str(user_input) + value,"." * need_to_fill, ''.join(reversed(value)) + str(user_input)
    print("".join(answer))
    need_to_fill -= 2




