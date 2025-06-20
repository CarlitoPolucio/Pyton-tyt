def string_normalize(__string: str) -> str:
    return "".join(["" if __string[i + 1] + x == "  " else x for i, x in enumerate(__string[:-1])])


if __name__ == '__main__':
    string = "У       нас         пошёл                    снег    ! "
    print(string_normalize(string))
    
