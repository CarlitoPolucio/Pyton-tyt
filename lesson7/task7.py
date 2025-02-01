user_input = input("Enter the numbers: ") + " "

num_sum = 0
num_to_print = 0
num_line = " "
line_to_print = " "

for num in user_input:
    if num == " ":
        if num_to_print < num_sum:
            num_to_print = num_sum
            line_to_print = num_line
        num_sum = 0
        num_line = " "
    else:
        num_line += num
        num_sum += int(num)

print(line_to_print, num_to_print)



