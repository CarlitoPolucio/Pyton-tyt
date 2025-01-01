a = int(input('Введите первое число: '))

b = int(input('Введите второе число: '))

print(a, b)

a = a - b
b = a + b
a = a // -1
a = a + b

# Альтернативный вариант:
# a += b
# b = a - b
# a -= b

print(a, b)