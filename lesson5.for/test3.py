y = int(input("Enter girls: "))
x = int(input("Enter boys: "))

if x / y > 2 or y / x > 2:
    print("unreal")
    exit()

BOY = str("B")
GIRL = str("G")

if x < y:
    x, y = y, x
    BOY, GIRL = GIRL, BOY

boy_counter = x
girl_counter = y

if x >= y:
    while boy_counter > 0:
        print(BOY, end="")
        boy_counter -= 1
        print(GIRL, end="")
        girl_counter -= 1
        if boy_counter != girl_counter:
            print(BOY, end="")
            boy_counter -= 1
        else:
            while girl_counter > 0:
                print(BOY, end="")
                boy_counter -= 1
                print(GIRL, end="")
                girl_counter -= 1
