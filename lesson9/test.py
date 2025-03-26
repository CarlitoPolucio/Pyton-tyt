def compression(__s: str) -> str:
    cipher, c = [], 0
    for i, sym in enumerate(__s):
        c += 1
        if i == len(__s) - 1 or sym != __s[i + 1]:
            cipher.append(f"{sym}{c}")
            c = 0
    return "".join(cipher)


if __name__ == '__main__':
    s = "ba]aajabbсaaj11"
    print(compression(s))





