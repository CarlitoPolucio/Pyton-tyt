from math import modf

def position(x, y):
    shit_x, pos_x = modf(x * 10)
    shit_y, pos_y = modf(y * 10)
    if not int(pos_x) in range(0, 8) or not int(pos_y in range(0, 8)):
        return main()
    return int(pos_x), int(pos_y)


def check_point(horse_pos_x, horse_pos_y, point_x, point_y):
    if point_y and point_x == horse_pos_y + 2 and horse_pos_x + 2:
        return "you cant"
    if point_y or point_x == horse_pos_y + 2 or horse_pos_x + 2:
        return "you can"
    return "you cant"


def main():
    horse_x = 0.234
    horse_y = 0.234
    p_x = 0.145
    p_y = 0.156
    horse_pos_x, horse_poz_y = position(horse_x, horse_y)
    point_pos_x, point_poz_y = position(p_x, p_y)
    print(check_point(horse_pos_x, horse_poz_y, point_pos_x, point_poz_y))

main()
