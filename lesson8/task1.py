def summa_n(number):
    return sum(range(1, number + 1))

user_number = 4
print(summa_n(user_number), summa_n(summa_n(user_number)))


