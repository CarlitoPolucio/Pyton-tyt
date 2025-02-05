depth = int(input("Enter the num: "))

left_digits = ""
right_output = ""
width = len("".join((str(i) for i in range(1, depth + 1)))) * 2

for i in range(depth, 0, -1):
    right_output = str(i) + right_output
    left_digits += str(i)
    print(left_digits + "." * (width - len(right_output) * 2) + right_output)




