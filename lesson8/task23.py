def position(a, b):
    position_a = (a // 100)
    position_b = (b // 100)
    if position_b == 0:
        position_b = 1
    if position_a == 0:
        position_a = 1
    return f"Figure is on ({position_a}, {position_b})"

def center_search(a, b):
    a = ((a // 100) * 100) + 50 - a
    b = ((b // 100) * 100) + 50 - b
    return f"Change position to: ({a},{b})"

horizontal = int(input("Enter horizontal: "))
vertical = int(input("Enter vertical: "))

if 0 <= horizontal <= 800 and 0 <= vertical <= 800 :
    print(position(horizontal, vertical), center_search(horizontal, vertical))
else:
    print("Error. There is no this coordinate.")
