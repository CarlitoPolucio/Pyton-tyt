def greeting():
    print('Привет!, Добро пожаловать!')

while True:
    a = input('Зайдёте? Да/Нет: ')
    if a == 'Да':
        greeting()
    print('Следующий.\n')