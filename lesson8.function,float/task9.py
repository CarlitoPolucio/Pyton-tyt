def sum_numbers(user_input):
    digit_sum = sum(int(digit) for digit in user_input)
    return digit_sum

def min_num(user_input):
    digit_min =  min(int(digit) for digit in user_input)
    return digit_min

def max_num(user_input):
    digit_max =  max(int(digit) for digit in user_input)
    return digit_max

while True:
    num = input("Enter the num: ")
    action = input("Choose what you want: get sum of nums(SUM), min num in number(MIN), or max num(MAX): ")
    if action == "SUM":
        answer = sum_numbers(num)
    elif action == "MIN":
        answer = min_num(num)
    elif action == "MAX":
        answer = max_num(num)
    else:
        print("Try again")
        continue
    print(answer)


