from _collections_abc import Iterable


def is_prime(check_num: int) -> bool:
    for num in range(2, round(check_num ** 0.5) + 1):
        if check_num % num == 0 and check_num != num:
            return False
    return True


def prime_list(iter_object: Iterable) -> list:
    return [value for i, value in enumerate(iter_object) if is_prime(i) and 1 != i != 0]


if __name__ == '__main__':
    user_list = list(range(0, 1500))
    print(prime_list(user_list))



