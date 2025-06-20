text = ("Светлоликий... приветствует вас в этом Днище."
        " Уже было сварито."
        " До краев земли налито."
        " Но еще не было отпито.")

step = 2
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
up = alphabet.upper()
step %= len(alphabet) // 2

print("".join([alphabet[alphabet.index(letter) + step] if letter in alphabet else letter for letter in text]))
main