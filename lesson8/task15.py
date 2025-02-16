def count_numbers(a, b):
    if len(a) < 3 or len(b) < 4:
        return False
    return True

def change_number(a, b):
    a = a[-1] + a[slice(1, len(a) - 1)] + a[0]
    b = b[-1] + b[slice(1, len(b) - 1)] + b[0]
    return f"Answer is {int(a) + int(b)}."

def main():
    first_num = input("Enter the first num: ")
    second_num = input("Enter the second num: ")
    if count_numbers(first_num, second_num):
        return change_number(first_num, second_num)
    else:
        return "Error"

print(main())





