def giga_sum(_list: list) -> int:
    opened = 0
    for element in _list:
        if str(element).isdigit():
            opened += element
        else:
            opened += giga_sum(element)
    return opened

if __name__ == '__main__':
    nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
    print(giga_sum(nice_list))