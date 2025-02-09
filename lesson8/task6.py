user_input = int(input("Enter the num: "))

from math import sqrt

divider_check = sqrt(user_input)

def is_prime(num):
    for dev_num in range(2, int(divider_check) + 1):
        if num == dev_num:
            continue
        elif num % dev_num == 0:
            return f"{num}: Составное."
    return f"{num}: Простое."

for number in range(2, user_input + 1):
    print(is_prime(number))
