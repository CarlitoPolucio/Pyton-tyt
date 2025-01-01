
first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
result = first_number % 100
result2 = second_number % 100
result3 = result2 + result
print(f"Последние две цифры первого числа: {result}")
print(f"Последние две цифры второго числа: {result2}")
print(f"Сумма этих чисел: {result3}")