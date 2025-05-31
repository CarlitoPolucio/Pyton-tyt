import os


def sum_nums(input_path: str) -> str:
    with open(input_path) as file:
        return str(sum(int(sym) for line in file for sym in line.split() if sym.isdigit()))


def to_write(_data: str, abs_path: str) -> None:
    with open(abs_path, mode="w") as file:
        file.write(_data)


if __name__ == '__main__':
    to_write(sum_nums(r"E:\github\lesson13.files\numbers.txt"), os.getcwd() + r"\answer.txt")