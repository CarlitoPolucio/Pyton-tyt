import random


class Human:
    DAY_PASSED = 0

    def __init__(self, name, house, satiety=50):
        self.name = name
        self.house = house
        self.satiety = satiety

    def eat(self, home):
        self.satiety += 10
        home.food -= 10

    def work(self, home):
        self.satiety -= 15
        home.money += 10

    def play(self):
        self.satiety -= 15

    @staticmethod
    def buy_food(home):
        home.food += 20
        home.money -= 10

class House:
    def __init__(self, food=50, money=50):
        self.food = food
        self.money = money

def play_model(residents: list, home):
    while Human.DAY_PASSED != 365:
        random_choice = random.randint(1, 5)
        if len(residents) == 0:
            print("Everyone is dead")
            break
        for person in residents:
            if person.satiety < 20:
                if person.satiety < 0:
                    residents.remove(person)
                    print(f"{person.name} is dead")
                    continue
                elif person.house.food < 10:
                    if person.house.money < 10:
                        person.work(home)
                    person.buy_food(home)
                person.eat(home)
            elif person.house.food < 10:
                person.buy_food(home)
            elif person.house.money < 50:
                person.work(home)
            elif random_choice == 1:
                person.work(home)
            elif random_choice == 2:
                person.eat(home)
            elif random_choice == 3:
                person.play()
        Human.DAY_PASSED += 1
        print(f"days passed: {Human.DAY_PASSED}, resources: money: {home.money}, food:{home.food}")
    print(f"365 days passed. {residents} stayed in house")


if __name__ == '__main__':
    home1 = House()
    person1 = Human("Семя", home1)
    person2 = Human("Данил", home1)
    play_model([person1,person2], home1)





