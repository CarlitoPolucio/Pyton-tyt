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

if x >= y:
    while x > 0:
        print(BOY, end="")
        x -= 1
        print(GIRL, end="")
        y -= 1
        if x != y:
            print(BOY, end="")
            x -= 1
        else:
            while y > 0:
                print(BOY, end="")
                x -= 1
                print(GIRL, end="")
                y -= 1


# QB, QG = int(input("B: ")), int(input("G: "))
# DOUBLE_MIN_Q, MAX_Q = min(QB, QG) * 2, max(QB, QG)
#
# if DOUBLE_MIN_Q < MAX_Q:
#     print("Impossible")
# else:
#     diff = abs(QB - QG)
#     if QB > QG:
#         pattern = "BGB"
#     else:
#         pattern = "GBG"
#     print(pattern * diff + "BG" * (DOUBLE_MIN_Q - MAX_Q))









