def numeral_count(user_input):
    amount_nums_checker = 0
    priority = ""
    while user_input > 0:
        user_input -= 1
        num = input("Enter the number: ")
        if int(num) < 0:
            priority = num
            continue
        if amount_nums_checker <= len(str(num)):
            amount_nums_checker = len(str(num))
            priority = num
    return priority

tasks = int(input("Enter the amount of tasks: "))
print(numeral_count(tasks))


