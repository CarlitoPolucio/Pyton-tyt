import logging

logger = logging.getLogger("answer")
logger.setLevel(logging.ERROR)

file_handler = logging.FileHandler("errors.log")
file_handler.setLevel(logging.ERROR)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class ValidationError(Exception):
    def __init__(self, message):
        self.message = message


def validation(_name: str, _i: int):
    if len(_name.strip()) < 3:
        raise ValidationError(f"ERROR: less than 3 sym in line {_i + 1}")


def get_data_collection(_path: str) -> int:
    with open(_path, mode="r", encoding="UTF-8") as users:
         all_sym = 0
         for i, line in enumerate(users):
             try:
                 validation(line, i)
             except ValidationError:
                 logger.error(f"ERROR1: less than 3 sym in line {i + 1}")
             all_sym += len(line.strip())
    return all_sym


if __name__ == '__main__':
    print(get_data_collection(r"E:\github\lesson14\01_names_2\people.txt"))





