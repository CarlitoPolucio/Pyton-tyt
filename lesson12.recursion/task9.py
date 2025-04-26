def rec_sort(_list: list) -> list:
    if len(_list) == 0:
        return _list
    bigger = []
    same = []
    smaller = []
    for num in _list:
        if num < _list[-1]:
            smaller.append(num)
        elif num > _list[-1]:
            bigger.append(num)
        else:
            same.append(num)
    bigger = rec_sort(bigger)
    smaller = rec_sort(smaller)
    return bigger + same + smaller


if __name__ == '__main__':
    to_sort = [5, 8, 9, 4, 2, 9, 1, 8]
    print(rec_sort(to_sort))