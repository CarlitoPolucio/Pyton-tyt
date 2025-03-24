text = "абвгдя"
step = 34
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
step %= len(alphabet) // 2
print([alphabet[alphabet.index(letter) + step] for letter in text])

