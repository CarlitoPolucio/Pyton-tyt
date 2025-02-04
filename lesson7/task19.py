user_input = int(input("Enter the num: "))

counter = 0
left_output = ""
dot_counter = ""
next_num = user_input
for dot in range(user_input + 1):
    dot_counter += str(dot)
need_to_fill = len(dot_counter) * 2 - 2

for num in range(1, user_input + 1):
    right_coordinate = user_input - counter
    output = range(right_coordinate, user_input + 1)
    right_output = ""
    for right_num in output:
        right_output += str(right_num)
    counter += 1
    left_output += str(next_num)
    full_output = (left_output, "." * (need_to_fill - len(left_output + right_output)), right_output)
    print("".join(full_output))
    next_num -= 1

# Рефакторинг + оптимизация
# depth = int(input("Enter the num: "))
#
# left_digits = ""
# right_output = ""
# width = len("".join((str(i) for i in range(1, depth + 1)))) * 2
#
# for i in range(depth, 0, -1):
#     right_output = str(i) + right_output
#     left_digits += str(i)
#     print(left_digits + "." * (width - len(right_output) * 2) + right_output)
