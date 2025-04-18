from math import modf


def position(x, y):
    shit_x, pos_x = modf(x * 10 + 1)
    shit_y, pos_y = modf(y * 10 + 1)
    if not int(pos_x) in range(0, 9) or not int(pos_y in range(0, 9)):
        return "Error"
    return int(pos_x), int(pos_y)


def check_point(horse_pos_x, horse_pos_y, point_x, point_y):
    if point_x == horse_pos_x or point_y == horse_pos_y:
        return "You cant"
    elif not point_y - horse_pos_y in range(-2, 3) or not point_x - horse_pos_x in range (-2, 3):
        return "You cant"
    elif ((point_x + point_y) - (horse_pos_x + horse_pos_y)) % 2 > 0:
        return "You can"
    else:
        return "You cant"


def main():
    horse_x = 0.455
    horse_y = 0.765
    p_x = 0.745
    p_y = 0.556
    horse_pos_x, horse_poz_y = position(horse_x, horse_y)
    point_pos_x, point_poz_y = position(p_x, p_y)
    print(check_point(horse_pos_x, horse_poz_y, point_pos_x, point_poz_y))


main()
