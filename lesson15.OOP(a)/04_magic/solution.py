class Element:
    def __init__(self, name=None):
        self.name = name

class Water(Element):
    def __add__(self, other):
        if other.name == "Огонь":
            return Steam("Пар")
        elif other.name == "Воздух":
            return Storm("Шторм")
        elif other.name == "Земля":
            return Mud("Грязь")
        return Mesivo()

class Air(Element):
    def __add__(self, other):
        if other.name == "Огонь":
            return Lightning("Молния")
        elif other.name == "Земля":
            return Dust("Пыль")
        else:
            return Mesivo()

class Fire(Element):
    def __add__(self, other):
        if other.name == "Земля":
            return Lava("Лава")
        return Mesivo()

class Mesivo(Element):
    pass

class Earth(Element):
    pass


class Lightning(Element):
    pass


class Steam(Element):
    pass


class Storm(Element):
    pass


class Lava(Element):
    pass


class Dust(Element):
    pass


class Mud(Element):
    pass


if __name__ == '__main__':
    water = Water("Вода")
    air = Air("Воздух")
    earth = Earth("Земля")
    fire = Fire("Огонь")
    result1 = water + fire
    result2 = water + air
    result3 = water + earth
    result4 = air + fire
    result5 = air + earth
    result6 = fire + fire
    print(result1.name, result2.name, result3.name, result4.name, result5.name, result6.name)
