## Тип данных int: целое число

Целые числа (int): представляют собой целые числа, как положительные, так и отрицательные.<br>
Например: 5, -3, 0.


## Арифметические операции
Python поддерживает стандартные арифметические операции:
- Сложение: +
- Вычитание: -
- Умножение: *
- Деление: / (результат всегда дробное число(об этом типе данных в следующих уроках))
- Возведение в степень: **
- Целочисленное деление //
- Остаток от деления %

```python
# Примеры операций с целыми числами
a = 10
b = 3

# Сложение
sum_result = a + b  # 13

# Вычитание
sub_result = a - b  # 7

# Умножение
mul_result = a * b  # 30

# Деление
div_result = a / b  # 3.3333...

# Возведение в степень
exp_result = a ** b  # 1000

# Целочисленное деление

floor_div_result = a // b  # 3


# Остаток от деления

mod_result = a % b  # 1
```

## Конкатенация строк с числами

В Python, если вы попытаетесь конкатенировать (объединить) строку (str) и целое число (int), вы получите ошибку типа TypeError.<br>
Это происходит потому, что Python не может автоматически преобразовать целое число в строку для выполнения операции конкатенации.

Вот пример, который демонстрирует эту ошибку:

```python
# Исправленный пример
name = "Alice"
age = 30

# Преобразование целого числа в строку
result = name + " is " + str(age) + " years old."
print(result)
```

При выполнении этого кода вы получите следующую ошибку:
```
TypeError: can only concatenate str (not "int") to str
```

Чтобы избежать этой ошибки, вы можете преобразовать целое число в строку с помощью функции str(). Вот исправленный пример:

```python
# Исправленный пример
name = "Alice"
age = 30

# Преобразование целого числа в строку
result = name + " is " + str(age) + " years old."
print(result)
```
Также можно использовать f-строки (форматированные строки) для более удобного форматирования:

```python
# Использование f-строк
result = f"{name} is {age} years old."
print(result)
```

## Приоритет арифметических операций

Приоритет арифметических операций в Python определяет порядок, в котором операции выполняются в выражениях.<br>
Если в одном выражении присутствуют несколько операций, Python будет выполнять их в соответствии с установленными правилами приоритета.
Вот список арифметических операций в порядке убывания приоритета:

1. Возведение в степень (**)
2. Унарный(знак числа) плюс и минус (+x, -x)
3. Умножение, деление, целочисленное деление и остаток от деления (*, /, //, %) (Об операциях // % в следующих уроках)
4. Сложение и вычитание (+, -)

### Правила приоритета
- Операции с более высоким приоритетом выполняются первыми.
- Если операции имеют одинаковый приоритет, они выполняются слева направо (ассоциативность слева направо), за исключением операции возведения в степень, которая ассоциативна справа налево.

### Использование скобок
Скобки могут использоваться для управления порядком выполнения операций. Выражения в скобках выполняются первыми:

```python
result = (2 + 3) * 4  # (2 + 3) * 4 = 5 * 4 = 20
print(result)  # Вывод: 20
```

## Пользовательский ввод числа
В Python для ввода данных с клавиатуры используется функция input().<br>
Эта функция позволяет пользователю ввести данные, которые затем можно использовать в программе.<br>
Важно помнить, что данные, введенные с помощью input(), всегда будут строкой (тип str).<br>
Если вам нужно работать с числами, вам нужно будет преобразовать введенные данные в соответствующий числовой тип (например, int или float).

Пример:
```python
# Ввод целого числа
user_input = input("Введите целое число: ")
number = int(user_input)  # Преобразование строки в целое число

print(f"Вы ввели число: {number}")
```

## Сокращение операций

В Python существуют сокращенные операции, которые позволяют выполнять операции и одновременно присваивать результат переменной.<br>
Пример:<br>
```python
a = 5
a += 3  # эквивалентно a = a + 3
print(a)  # 8
```
Вместо оператора + здесь мог бы быть любой другой арифметический оператор.