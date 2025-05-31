import os

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def freq_analys(_path: str) -> None:
    with open(_path, mode="r") as letters:
        content = "".join([sym for sym in letters.read().lower() if sym in ALPHABET])
        letters_data_sort({letter: round((content.count(letter.lower()) / len(content)) * 100, 3) for letter in ALPHABET})


def letters_data_sort(_letters_dict: dict[str, float]) -> None:
    with open(os.path.join(os.getcwd(), "analysis.txt"), mode="w") as analyzed_file:
        for letter_inf in(sorted(sorted(_letters_dict.items(), key=lambda letter: letter[0]), key=lambda letter: letter[1], reverse=True)):
            analyzed_file.write(letter_inf[0] +  ": " + str(letter_inf[1]) + "\n")


if __name__ == '__main__':
    print(freq_analys(r"E:\github\lesson13.files\text.txt"))