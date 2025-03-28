def slicing(__first_string: str, __second_string: str) -> bool:
    for i, sym in enumerate(__second_string):
        if __second_string.count(sym) != __first_string.count(sym):
            return False
        elif __second_string[-i:] + __second_string[:-i] == __first_string:
            return True
    return False


if __name__ == '__main__':
    a = "baababba"
    b = "cabbabaab"
    print(slicing(a, b))


