def dictionary(__num: int) -> dict:
    return {key: key ** 2 for key in range(1, __num)}


if __name__ == '__main__':
    num = 5
    print(dictionary(num))