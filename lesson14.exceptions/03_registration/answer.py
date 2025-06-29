import logging

error_logger = logging.getLogger("error_logger")
error_logger.setLevel(logging.ERROR)

error_handler = logging.FileHandler("registrations_bad.log")
error_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
error_logger.addHandler(error_handler)

info_logger = logging.getLogger("info_logger")
info_logger.setLevel(logging.INFO)

info_handler = logging.FileHandler("registrations_good.log")
info_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
info_logger.addHandler(info_handler)

class ValidationError(Exception):
    pass


def email_valid(_email: str) -> None:
    if "@" in _email and "." in _email:
        return
    error_logger.error("The ''Email'' field does NOT contain @ and/or . (dot)")
    raise ValidationError


def age_valid(_age: str) -> None:
    if _age.isdigit() and int(_age) in range(10, 100):
        return
    error_logger.error("The Age field is NOT a number between 10 and 99")
    raise ValidationError


def name_valid(_name: str) -> None:
    for sym in _name:
        if sym.isdigit():
            error_logger.error("The ''Name'' field does NOT contain only letters")
            raise ValidationError
    return


def fields_quantity(_line: str):
    if len(_line.split()) != 3:
        error_logger.error("All three fields are NOT present")
        raise ValidationError
    return


if __name__ == '__main__':

    def users_info_check(_path: str):
        with open(_path, mode="r") as file:
            for line in file:
                try:
                    fields_quantity(line)
                except ValidationError as e:
                    error_logger.error(f"Validation Error. Wrong fields in line {line}")
                    continue
                try:
                    {k: func(k) for k, func in zip(line.split(), (name_valid, email_valid, age_valid))}
                except ValidationError as e:
                    error_logger.error(f"Validation Error: {e} in line {line}")
                    continue
                info_logger.info(line)


    users_info_check(r"E:\github\lesson14\03_registration\registrations.txt")



