QB, QG = int(input("B: ")), int(input("G: "))
DOUBLE_MIN_Q, MAX_Q = min(QB, QG) * 2, max(QB, QG)

if DOUBLE_MIN_Q < MAX_Q:
    print("Impossible")
else:
    diff = abs(QB - QG)
    if QB > QG:
        pattern = "BGB"
    else:
        pattern = "GBG"
    print(pattern * diff + "BG" * (DOUBLE_MIN_Q - MAX_Q))



















