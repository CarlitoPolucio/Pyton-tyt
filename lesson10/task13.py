def palindrom(__text: str) -> bool:
    check = [1 if __text.count(x) % 2 == 0 or x == " " else 2 for x in __text]
    if check.count(2) > 1:
        return False
    return True

if __name__ == '__main__':
    text = "Гни, комсомол, лом о смокинг"
    print(palindrom(text.lower()))

