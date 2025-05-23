## Вложенные циклы

Вложенный цикл for — это цикл, который находится внутри другого цикла for.<br>
Внешний цикл выполняется первый, и для каждой итерации внешнего цикла внутренний цикл выполняется полностью.

```python
for i in range(3):  # Внешний цикл
    for j in range(2):  # Внутренний цикл
        print(f"i = {i}, j = {j}")
```
```text
i = 0, j = 0
i = 0, j = 1
i = 1, j = 0
i = 1, j = 1
i = 2, j = 0
i = 2, j = 1

Здесь внешний цикл выполняется 3 раза (для i = 0, 1, 2), и для каждого значения i внутренний цикл выполняется 2 раза (для j = 0, 1).
```

### Вложенные циклы с условиями

```python
for i in range(1, 4):  # Внешний цикл
    for j in range(1, 4):  # Внутренний цикл
        if i == j:
            print(f"i = {i}, j = {j} -> На главной диагонали")
        else:
            print(f"i = {i}, j = {j}")
```

```text
i = 1, j = 1 -> На главной диагонали
i = 1, j = 2
i = 1, j = 3
i = 2, j = 1
i = 2, j = 2 -> На главной диагонали
i = 2, j = 3
i = 3, j = 1
i = 3, j = 2
i = 3, j = 3 -> На главной диагонали

Здесь вложенные циклы используются для проверки, находятся ли индексы на главной диагонали (когда i == j).
```

### Примечания
- Вложенные циклы могут быть медленными, особенно если количество итераций велико. Если возможно, старайтесь оптимизировать код, чтобы избежать глубокой вложенности.
- Слишком много вложенных циклов могут сделать код сложным для понимания. Если вложенность становится слишком глубокой, подумайте о рефакторинге кода.
- break и continue могут использоваться внутри вложенных циклов для управления потоком выполнения. break завершает выполнение ближайшего цикла, а continue переходит к следующей итерации ближайшего цикла.

```python
for i in range(3):
    for j in range(3):
        if i == j:
            break  # Прерывает внутренний цикл, если i == j
        print(f"i = {i}, j = {j}")
```
```text
i = 1, j = 0
i = 2, j = 0
i = 2, j = 1

Здесь внутренний цикл прерывается, когда i == j, и выполнение продолжается с внешним циклом.
```

## Литерал табуляции /t
В Python, как и во многих других языках программирования, символ \t представляет собой литерал табуляции. Это escape-последовательность, которая используется для вставки символа табуляции в строку.<br>

Когда интерпретатор Python встречает \t в строке, он заменяет его на символ табуляции (горизонтальный отступ).<br>
Табуляция обычно эквивалентна нескольким пробелам (часто 4 или 8, в зависимости от настроек редактора или терминала).

Табуляция полезна для выравнивания текста, например, при создании таблиц или отступов.<br>
Использование табуляции может сделать вывод более структурированным и удобным для чтения.


```python
print("Name\tAge\tCity")
print("John\t23\tNew York")
print("Alice\t30\tLos Angeles")
```

```text
Name    Age     City
John    23      New York
Alice   30      Los Angeles
```

```python
print("First line\tSecond line\nThird line\tFourth line")
```
```text
First line   Second line
Third line   Fourth line
```

Можно сказать, что табуляция "растворяется" в строке в том смысле, что она динамически подстраивается под длину текста, чтобы достичь следующей фиксированной позиции табуляции. Если строка длиннее, чем текущая позиция табуляции, табуляция просто добавляет необходимое количество пробелов, чтобы "дотянуть" до следующей позиции.
Позиции табуляции задаются через фиксированные интервалы (например, каждые 4, 8 или 16 символов).

Например, если табуляция равна 4 символам, позиции будут: 4, 8, 12, 16, 20 и т.д.
Когда встречается символ табуляции (\t), программа вычисляет, сколько пробелов нужно добавить, чтобы достичь следующей позиции табуляции.
Если текст перед \t уже занимает часть позиции, добавляются только оставшиеся пробелы.
Если текст перед \t превышает текущую позицию табуляции, табуляция просто перемещает курсор к следующей позиции.

```text
Предположим, табуляция равна 4 символам, тогда:
    - Позиции табуляции: 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, ...
    - Строка This is a very long string that exceeds multiple tab stops занимает 52 символа.
    - Следующая позиция табуляции после 52 символов — это 56.
    - \t добавляет 4 пробела, чтобы достичь позиции 56.
   
```
Тогда:

```python
print("This is a very long string that exceeds multiple tab stops\tText")
```
```text
This is a very long string that exceeds multiple tab stops    Text
```

### Примечания
- Табуляция (\t) и пробелы — это разные символы.
- В некоторых случаях (например, в конфигурационных файлах или коде) использование пробелов предпочтительнее, чтобы избежать проблем с разными редакторами, которые могут по-разному интерпретировать табуляцию.

### Экранирование
Экранирование в Python — это механизм, который позволяет использовать специальные символы в строках, не нарушая синтаксис языка. Специальные символы (например, кавычки, символы новой строки, табуляции и т.д.) интерпретируются Python особым образом. Чтобы использовать их как обычные символы, нужно их экранировать.

Экранирование выполняется с помощью обратного слэша (\). Когда Python встречает \, он интерпретирует следующий символ как обычный символ, а не как специальный.

```python
text = "Он сказал: \"Привет!\""  # Экранирование кавычек
print(text)
```
```text
Он сказал: "Привет!"
```
```python
path = "C:\\Users\\Username\\Documents"
print(path)
```
```text
C:\Users\Username\Documents
```
```python
text = "Имя\tВозраст\tГород\nАлиса\t30\tМосква"
print(text)
```
```text
Имя    Возраст    Город
Алиса  30         Москва
```

### Сырые строки
Если вам нужно использовать много обратных слэшей (например, в регулярных выражениях или путях к файлам), можно использовать сырые строки (raw strings). В сырых строках экранирование отключено.
```python
path = r"C:\Users\Username\Documents"
print(path)
```
```text
C:\Users\Username\Documents
```

### Экранирование в тройных кавычках

Тройные кавычки (''' или """) позволяют создавать многострочные строки. Внутри них можно использовать кавычки без экранирования, но обратные слэши всё ещё нужно экранировать.

```python
text = """Это строка с "двойными" и 'одинарными' кавычками."""
print(text)
```

```text
Это строка с "двойными" и 'одинарными' кавычками.
```

