def cipher(__text: str) -> str:
    output = ""
    count = 0
    sym  = __text[0]
    for i, x in enumerate(__text):
        if x == sym:
            count += 1
        else:
            output += sym + str(count)
            count = 1
            sym = x
    output += sym + str(count)
    return output


if __name__ == '__main__':
    s = 'aaaabbttKKttсaa'
    print(cipher(s))