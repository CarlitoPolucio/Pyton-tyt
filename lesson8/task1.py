user_input = int(input("Enter the num: "))

number = 0

def summa_n():
    return sum(range(number, 0, -1))

number += user_input
print(summa_n())
number = summa_n()
print(summa_n())