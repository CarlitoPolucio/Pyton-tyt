from random import choice


class Parent:
    def __init__(self, name, age, children: list):
        self.name = name
        self.age = age
        self.children = children


    def get_parent_inf(self):
        return f"My name is {self.name}, I am {self.age}, My children: {self.children}"

    @staticmethod
    def calm_child(_child):
        child.calm = False
        return child.calm

    @staticmethod
    def feed_child(_child):
        child.hunger = False
        return child.hunger

    def get_age(self):
        return self.age


class Child:
    def __init__(self, name, age, calm = True, hunger = True):
        self.name = name
        self.age = age
        self.calm = calm
        self.hunger = hunger

    def get_hunger_inf(self):
        self.hunger = choice([True, False])
        return self.hunger

    def get_calm_inf(self):
        self.calm = choice([True, False])
        return self.calm


if __name__ == '__main__':
    child1 = Child("Захар", 16)
    child2 = Child("Вобля", 6)
    parent1 = Parent("Семя", 23, [child1, child2])

    for child in [child1,child2]:
        if child.get_calm_inf():
            parent1.calm_child(child)
            print(f"{child.name} has been calmed")
        else:
            print(f"{child.name} is already calm")
        if child.get_hunger_inf():
            parent1.feed_child(child)
            print(f"{child.name} has been fed")
        else:
            print(f"{child.name} is already fed")

    print(parent1.get_parent_inf())















