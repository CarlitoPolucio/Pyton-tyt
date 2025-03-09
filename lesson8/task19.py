def format_num(num):
    if float(num) < 1:
        q_dividers = len(num) - 3
        return f"x = {float(num) * 10 ** q_dividers} * {10} ** {q_dividers * -1}"
    q_dividers = len(num) - 1
    return f"x = {float(num) / 10 ** q_dividers} * {10} ** {q_dividers}"

x = "0.0012"
print(format_num(x))