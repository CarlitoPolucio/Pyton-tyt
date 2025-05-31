import os
import zipfile

ALPHABET = [
    'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',

]


def freq_analys(_path: str) -> None:
    with zipfile.ZipFile(_path) as _zip:
        _zip.extract("voyna-i-mir.txt")
        _path = os.path.join(os.getcwd(), "voyna-i-mir.txt")
    with open(_path, mode="r", encoding="UTF-8") as letters:
        content = "".join([sym for sym in letters.read() if sym in ALPHABET])
        letters_data_sort({letter: round((content.count(letter) / len(content)) * 100, 3) for letter in ALPHABET})


def letters_data_sort(_letters_dict: dict[str, float]) -> None:
    with open(os.path.join(os.getcwd(), "analys_voyni.txt"), mode="w", encoding="UTF-8") as analyzed_file:
        for letter_inf in(sorted(sorted(_letters_dict.items(), key=lambda letter: letter[0]), key=lambda letter: letter[1], reverse=True)):
            analyzed_file.write(letter_inf[0] +  ": " + str(letter_inf[1]) + "\n")


if __name__ == '__main__':
    print(freq_analys(r"E:\github\lesson13.files\voyna-i-mir.zip"))