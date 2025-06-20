rad = float(input("enter the radius: "))

from math import pi

def sphere_area():
    return (4 * pi) * rad ** 2

def sphere_volume():
    return ((4 / 3) * pi) * rad ** 3

print(f"Area is: {sphere_area()}, volume is: {sphere_volume()}")

