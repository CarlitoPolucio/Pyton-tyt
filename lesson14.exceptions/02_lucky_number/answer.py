from random import randint


class RandomValidation(Exception):
    def __init__(self, massage: str):
        self.massage = massage


def input_processing(user_num, random_result: bool, _total: float) -> [float, int]:
    if not user_num.isdigit():
        return 0
    with open("out_file.txt", mode="a") as file:
        if random_result:
            file.write(f"{user_num}\n")
            if float(user_num) + _total >= 777:
                print("Вы успешно выполнили условие для выхода из порочного цикла!")
                exit()
            else:
                return user_num
        print("Вас постигла неудача!")
        raise RandomValidation("Shit happens")


def random_num(_probability: int) -> bool:
    if randint(1, _probability) == 1:
        return False
    return True


if __name__ == '__main__':
    total = 0
    while True:
        user_result = input_processing(input("Введите число: "), random_num(13), total)
        if user_result == 0:
            print("Use digits")
            continue
        total += float(user_result)