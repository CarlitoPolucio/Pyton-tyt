## Задача 1. Таблица степеней

Реализуйте бесконечный цикл. 

Структура итерации:
- запроса целого числа
- добавления элемента в список
- вывод 2, 3, 4 степней каждого элемента списка

## Задача 2. Поиск максимального числа
Реализуйте собственный алгоритм нахождения максимального целого числа в списке. Функция принимает на вход массив целых чисел и возвращает значение максимального числа. Нельзя применять готовые функции типа built-in(встроенных) или third-party(сторонних).

## Задача 3. Рокировка крайностей
Дан список очков из N целых чисел. Напишите функцию, которая меняет местами набольшее с наименьшим.

## Задача 4. Кратность
Пользователь вводит список из N чисел и число K. Напишите функцию, выводящую на экран сумму индексов элементов списка, которые кратны K.

<details>
    <summary>Совет по оптимизации(Рекомендуется раскрыть после собственной реализации)</summary> 
    Примените функцию enumerate к списку
</details>

## Задача 5. Текстовый редактор 2
Пользователь вводит строку S. Напишите программу, которая заменяет в строке все двоеточия (:) на точки с запятой (;). Также подсчитайте количество замен и выведите ответ на экран (и новую строку тоже). Для решения используйте список.

## Задача 6. Удаление максимума
Напишите функцию, которая удаляет из списка целых чисел максимальный элемент.

## Задача 7. Порядок
```python
nums = [5, 4, 3, 3, 2, 1]
```
Числа выстроены в ряд по убыванию.

Получите на вход целое число и внесите в имеющийся список не нарушая порядок.

## Задача 8. Цикличность
Дан список из N целых чисел и целое число K. Напишите программу, которая циклически сдвигает элементы списка вправо на K позиций.
```text
Сдвиг: 3

Изначальный список: [1, 4, –3, 0, 10]

Сдвинутый список: [–3, 0, 10, 1, 4]
```

## Задача 9. Бинарный поиск**
Реализуйте алгоритм бинарного поиска с применением списка. Функция получает на вход *подготовленный* массив целых чисел и значение искомого элемента. Функция возвращает индекс искомого элемента или None.

## Задача 10. Алгоритм сортировки***
Дан список из N чисел. Напишите программу, которая сортирует элементы списка по возрастанию и выводит их на экран. Дополнительный список использовать нельзя.
Также нельзя использовать готовые функции sorted/min/max и метод sort
