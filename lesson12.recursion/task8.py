def open_list(_list: list) -> list:
    opened = []
    for element in _list:
        if str(element).isdigit():
            opened.append(element)
        else:
            opened += open_list(element)
    return opened


if __name__ == '__main__':
    nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]

    print(open_list(nice_list))