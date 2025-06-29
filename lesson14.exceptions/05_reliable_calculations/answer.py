import math


def sqrt(_num: float) -> [float | str]:
    try:
        return math.sqrt(_num)
    except ValueError:
        return f"Error: negative number: {_num}"
    except TypeError:
        return f"Wrong type error. Expect number type: 'Int'|'float' got {type(_num).__name__} instead"
    except Exception as _e:
        return f"Unexpected error {_e}"


if __name__ == '__main__':
    try:
        print(sqrt(36))
    except NameError as e:
        print(f"Enter error {e}")


