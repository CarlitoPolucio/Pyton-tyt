import random

class Units:
   _DAMAGE = 20

   def __init__(self, health: int, name: str):
       self.health = health
       self.name = name


   def get_damage(self):
       self.health -= self._DAMAGE
       if self.health <= 0:
           return True
       print(f"The warrior {self.name} has {self.health} left")


if __name__ == '__main__':
    green_warrior = Units(100, "Zahar")
    red_warrior = Units(100, "Danil")
    while True:
        fight_list = [green_warrior,red_warrior]
        attacker = fight_list.pop(random.randint(0,1))
        if fight_list[0].get_damage():
            print(f"Warrior {attacker.name} killed {fight_list[0].name}")
            exit()
        print(f"The Warrior {attacker.name} hit {fight_list[0].name} by 20 damage")





