import string


def password_check(__password: str) -> bool:
    allow = string.ascii_lowercase + string.ascii_uppercase + string.digits
    for sym in __password:
        if sym in allow:
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