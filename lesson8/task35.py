from math import modf

def position(x, y):
    shit_x, pos_x = modf(x * 10)
    shit_y, pos_y = modf(y * 10)
    if not int(pos_x) in range(0, 8) or not int(pos_y in range(0, 8)):
        return main()
    return int(pos_x), int(pos_y)


def check_point(horse_pos_x, horse_pos_y, point_x, point_y):
    if (point_x == horse_pos_x - 2 or point_x == horse_pos_x + 2 and point_y == horse_pos_y - 2
        or point_y == horse_pos_y + 2 or point_x == horse_pos_x or point_y == horse_pos_y):
        return print("You cant"), main()
    if point_x in range(horse_pos_x - 2, horse_pos_x + 3):
        if point_y in range(horse_pos_y - 2, horse_pos_y + 3):
            return print("You can"), main()


def main():
    horse_x = float(input("Enter horse position x: "))
    horse_y = float(input("Enter horse position y: "))
    p_x = float(input("Enter position x: "))
    p_y = float(input("Enter position y: "))
    horse_pos_x, horse_poz_y = position(horse_x, horse_y)
    point_pos_x, point_poz_y = position(p_x, p_y)
    print(check_point(horse_pos_x, horse_poz_y, point_pos_x, point_poz_y))

main()








