## Булевый тип данных (bool)
Булевый тип данных (или логический тип) в Python представляет собой тип, который может принимать только два значения: True (истина) и False (ложь). Этот тип данных используется для выполнения логических операций и управления потоком выполнения программы.
В Python булевый тип данных представлен двумя константами:
```text
True — логическая истина.
False — логическая ложь.
```

### Преобразование в булевый тип
Вы можете преобразовать другие типы данных в булевый тип с помощью функции bool().<br>
Вот несколько базовых примеров возможных преобразований:
```python
print(bool(0))          # False
print(bool(1))          # True
print(bool(""))         # False
print(bool("Hello"))    # True
```
### Примечание
Булевый тип данных в Python является подтипом целочисленного типа. Это означает, что True эквивалентен числу 1, а False эквивалентен числу 0.
```python
print(True == 1)   # True
print(False == 0)  # True
```
Об операции сравнения ниже


## Операторы сравнения.
Операторы сравнения в Python используются для сравнения значений и возвращают логическое значение(булевый тип данных) True или False. Эти операторы позволяют выполнять различные проверки, такие как равенство, неравенство, больше или меньше и т.д. Вот основные операторы сравнения в Python:<br>

| Оператор | Описание                          | Пример          | Результат |
|----------|-----------------------------------|-----------------|-----------|
| `==`     | Равенство                         | `5 == 5`        | `True`    |
| `!=`     | Неравенство                       | `5 != 3`        | `True`    |
| `>`      | Больше                            | `5 > 3`         | `True`    |
| `<`      | Меньше                            | `5 < 8`         | `True`    |
| `>=`     | Больше или равно                 | `5 >= 5`        | `True`    |
| `<=`     | Меньше или равно                 | `5 <= 8`        | `True`    |

## Условный оператор if
Условный оператор if в Python используется для выполнения определенного блока кода, если заданное условие истинно (True). Это позволяет программе принимать решения и выполнять разные действия в зависимости от условий.
```python
x = 10

if x > 5:
    print(f"{x} больше 5")
```

## Условный оператор else
Оператор else в Python используется в сочетании с условными операторами, такими как if и elif, для выполнения блока кода, когда все предыдущие условия не были истинными. Это позволяет задать альтернативное действие, если ни одно из условий не выполнено.

```python
x = 3

if x > 5:
    print(f"{x} больше 5")
else:
    print(f"{x} меньше 5")
```

## Условный оператор elif
Оператор elif в Python используется в условных конструкциях для проверки дополнительных условий, если предыдущее условие не было истинным. Это сокращение от "else if" и позволяет создавать более сложные логические ветвления в коде.


```python
x = 3

if x > 5:
    print(f"{x} больше 5")
elif x == 5:
    print(f"{x} равно 5")
else:
    print(f"{x} меньше 5")
```

## Вложенные условия
Вложенные условия в Python — это конструкции, в которых один оператор if (или elif, else) находится внутри другого оператора if. Это позволяет создавать более сложные логические проверки и управлять потоком выполнения программы в зависимости от нескольких условий.
```python
age = 20
has_permission = True

if age >= 18:
    print("Вы совершеннолетний.")
    if has_permission:
        print("Доступ разрешен.")
    else:
        print("Доступ запрещен.")
else:
    print("Вы несовершеннолетний.")
```

```text
Сначала проверяется, является ли age больше или равным 18.
Если это условие истинно, программа проверяет, есть ли у человека разрешение (has_permission).
В зависимости от значения has_permission программа выводит соответствующее сообщение.
```

```python
score = 85

if score >= 90:
    print("Отлично!")
elif score >= 75:
    print("Хорошо!")
    if score >= 80:
        print("Вы находитесь в верхней половине группы.")
    else:
        print("Вы находитесь в нижней половине группы.")
else:
    print("Неудовлетворительно.")
```
```text
Сначала проверяется, является ли score больше или равным 90.
Если это условие ложно, проверяется, является ли score больше или равным 75.
Если это условие истинно, выполняется дополнительная проверка, чтобы определить, находится ли score в верхней или нижней половине группы.
```

### Примечания
- Вложенные условия могут сделать код менее читаемым, особенно если уровни вложенности становятся слишком глубокими. Поэтому по возможности вложенные условия принято избегать.

## Логические операторы or and not
Операторы or, and и not в Python — это логические операторы, которые используются для выполнения логических операций над булевыми значениями (True и False). Они позволяют комбинировать логические выражения и управлять потоком выполнения программы. Давайте рассмотрим каждый из этих операторов подробнее.

### Логический оператор and
Оператор and возвращает True, если оба операнда истинны. Если хотя бы один из операндов ложен, результат будет False.
```python
a = True
b = False

result = a and b  # False, так как b ложен
```

```python
age = 20
has_permission = True

if age >= 18 and has_permission:
    print("Доступ разрешен.")
else:
    print("Доступ запрещен.")
```

### Логический оператор or
Оператор or возвращает True, если хотя бы один из операндов истинен. Если оба операнда ложны, результат будет False.

```python
a = True
b = False

result = a or b  # True, так как a истинен
```

```python
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("Можно отдохнуть!")
else:
    print("Время работать.")
```

### Логический оператор not
Оператор not инвертирует логическое значение. Если операнд истинен, not вернет False, и наоборот.

```python
a = True

result = not a  # False
```

```python
is_logged_in = False

if not is_logged_in:
    print("Пожалуйста, войдите в систему.")
```

### Приоритет логических операций
Важно помнить о приоритете логических операторов. Оператор not имеет более высокий приоритет, чем and, а and имеет более высокий приоритет, чем or. Это означает, что выражения будут вычисляться в следующем порядке:
```python
a = True
b = False
c = True

result = a or b and c  # Результат будет True, так как b and c вычисляется первым
```

### Таблица истинности
В дополнение можно рассмотреть таблицу истинности:

| A     | B     | A and B | A or B | not A |
|-------|-------|---------|--------|-------|
| True  | True  | True    | True   | False |
| True  | False | False   | True   | False |
| False | True  | False   | True   | True  |
| False | False | False   | False  | True  |