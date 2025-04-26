# os
Модуль os в Python предоставляет множество функций для взаимодействия с операционной системой, включая работу с файлами, директориями, переменными окружения и процессами.
- os.getcwd() – возвращает текущую рабочую директорию.
- os.chdir(path) – изменяет текущую директорию на path.
- os.listdir(path='.') – возвращает список файлов и директорий в указанной директории.
- os.mkdir(path) – создаёт директорию по указанному пути.
- os.makedirs(path) – создаёт директорию рекурсивно (включая все промежуточные папки).
- os.remove(path) – удаляет файл.
- os.rmdir(path) – удаляет пустую директорию.
- os.removedirs(path) – удаляет директорию рекурсивно.
- os.rename(src, dst) – переименовывает файл или директорию.
- os.path.exists(path) – проверяет, существует ли файл или директория.
- os.path.isfile(path) – проверяет, является ли путь файлом.
- os.path.isdir(path) – проверяет, является ли путь директорией.
- os.path.join(path1, path2, ...) – объединяет пути с учётом ОС.
- os.path.abspath(path) – возвращает абсолютный путь.
- os.path.basename(path) – возвращает имя файла или директории из пути.
- os.path.dirname(path) – возвращает родительскую директорию.
- os.path.split(path) – разделяет путь на (директория, имя_файла).
## Работа с переменными окружения
- os.environ – словарь с переменными окружения.
- os.getenv(key, default=None) – возвращает значение переменной окружения key (если нет – default).
- os.putenv(key, value) – устанавливает переменную окружения (не рекомендуется, лучше менять os.environ).
## Управление процессами
- os.system(command) – выполняет команду в shell (возвращает код завершения).
- os.startfile(path) – открывает файл в ассоциированной программе (Windows).
- os.popen(command) – выполняет команду и возвращает файлоподобный объект для чтения вывода (устаревший, лучше subprocess).
- os.getpid() – возвращает ID текущего процесса.
- os.getppid() – возвращает ID родительского процесса.
- os.kill(pid, signal) – отправляет сигнал процессу.
## Дополнительные функции
- os.name – имя ОС ('posix', 'nt', 'java').
- os.sep – разделитель пути (/ или \).
- os.linesep – разделитель строк (\n, \r\n).
- os.urandom(n) – возвращает n случайных байт.
```python
import os

# Работа с файлами
print(os.getcwd())  # Текущая директория
os.chdir("/tmp")    # Смена директории
print(os.listdir()) # Список файлов

# Создание и удаление директорий
os.mkdir("test_dir")
os.rmdir("test_dir")

# Проверка существования файла
if os.path.exists("file.txt"):
    print("Файл существует")

# Работа с путями
path = os.path.join("folder", "subfolder", "file.txt")
print(path)  # folder/subfolder/file.txt (или folder\subfolder\file.txt на Windows)

# Переменные окружения
print(os.getenv("HOME"))  # /home/user (Linux)
os.environ["MY_VAR"] = "123"

# Запуск команды
os.system("ls -l")  # Выполнить команду в shell
```
## Модуль os.path
```python
import os.path

path = "/home/user/file.txt"
print(os.path.dirname(path))   # /home/user
print(os.path.basename(path)) # file.txt
print(os.path.split(path))    # ('/home/user', 'file.txt')
print(os.path.splitext(path)) # ('/home/user/file', '.txt')
```

# open
Функция open() используется для работы с файлами: чтение, запись, создание и модификация. Это одна из самых важных функций в Python для ввода-вывода данных.
```python
file = open("file", mode='r', encoding=None, buffering=-1, errors=None, newline=None, closefd=True, opener=None)
```
- file – путь к файлу (строка или байты).
- mode – режим открытия ('r', 'w', 'a', 'b', '+' и др.).
- encoding – кодировка ('utf-8', 'cp1251', 'ascii' и др.).
- buffering – буферизация (0 – нет, 1 – построчная, >1 – размер буфера).
- errors – обработка ошибок кодировки ('strict', 'ignore', 'replace').
- newline – управление переводом строк (None, '\n', '\r\n').
- Режимы открытия файла:
  - 'r'	Чтение (по умолчанию). Файл должен существовать.
  - 'w'	Запись. Если файл существует, он перезаписывается. Если нет – создаётся.
  - 'a'	Дозапись в конец файла. Если файла нет – создаётся.
  - 'x'	Эксклюзивное создание. Если файл существует – ошибка FileExistsError.
  - 'b'	Бинарный режим ('rb', 'wb', 'ab').
  - 't'	Текстовый режим (по умолчанию).
  - '+'	Открытие для чтения и записи ('r+', 'w+', 'a+').
## Основные методы работы с файлом
- Чтение:
```python
file = open("file", mode='r', encoding=None, buffering=-1, errors=None, newline=None, closefd=True, opener=None)
with open("file.txt", "r") as f:
    content = f.read()  # Читает весь файл
    line = f.readline() # Читает одну строку
    lines = f.readlines() # Читает все строки в список
with open("file.txt", "w") as f:
    f.write("Hello, World!\n") # Записывает строку или байты
    f.writelines(["Line 1\n", "Line 2\n"]) # Записывает список строк
```
```text
file.seek(offset)     # Перемещает курсор на `offset` байт
file.tell()           # Возвращает текущую позицию курсора
file.flush()          # Принудительно записывает данные на диск
file.close()          # Закрывает файл (лучше использовать `with`!)
```
- Использование with (контекстный менеджер)
Автоматически закрывает файл после блока:
```python
with open("file.txt", "r") as f:
    data = f.read()
# Файл закрыт автоматически
```
- Обработка разных кодировок
```python
with open("file.txt", "r", encoding="utf-8") as f:
    text = f.read()
```
- Чтение файла построчно (экономно по памяти)
```python
with open("large_file.txt", "r") as f:
    for line in f:  # Читает по одной строке
        print(line.strip())
```
