def reg_check(__text: str) -> str:
    return __text.upper() if len([x for x in __text if x.islower()]) < len([x for x in __text if x.isupper()]) else __text.lower()


if __name__ == '__main__':
    text = "AAAAaaa"
    print(reg_check(text))
