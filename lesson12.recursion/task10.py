def rec_bin_search(numbers_list: list, secret: int) -> int | None:
    mid = len(numbers_list) // 2
    if len(numbers_list) == 1 and numbers_list[mid] != secret:
        return
    if secret > numbers_list[mid]:
        return rec_bin_search(numbers_list[mid:], secret)
    elif secret < numbers_list[mid]:
        return rec_bin_search(numbers_list[:mid], secret)
    else:
        return numbers_list[mid]


if __name__ == '__main__':
    nums_list = list(range(-200, 200, 5))
    print(rec_bin_search(nums_list, -40))