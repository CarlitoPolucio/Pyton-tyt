import string


ALLOW = string.ascii_lowercase + string.ascii_uppercase + string.digits


def password_check(__password: str) -> bool:
    for sym in __password:
        if sym not in ALLOW:
            return False
    if len(__password) >= 8 and len([x for x in __password if x.isupper()]) >= 1 and len([x for x in __password if x.isdigit()]) >= 3:
        return True
    return False


def sign_up():
    while True:
        user_password = input("Password: ")
        if password_check(user_password):
            return True


if __name__ == '__main__':
    sign_up()