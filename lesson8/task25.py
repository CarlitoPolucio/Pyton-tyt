def x_line(s, cos):
    return s * cos


def y_line(s, sin):
    return s * sin


x = 0
y = 0

while True:
    x_dist_in = int(input("Enter distance x: "))
    x_cos_in = int(input("Enter angle x: "))
    y_dist_in = int(input("Enter distance and the distance y: "))
    y_sin_in = int(input("Enter distance and the angle y: "))
    print(x_line(x_dist_in, x_cos_in), ",", y_line(y_dist_in, y_sin_in))
