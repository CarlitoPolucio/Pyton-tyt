money = int(input("Amount of money "))

CHEESE = 60
ICECREAM = 20

if 80 > money >= 60:
    cheese_buy = money - 60
    print("You just bought the cheese, but you don't have enough money to buy an icecream")
elif 60 > money:
    print("you don't have enough money to buy anything.")
else:
    print("You have enough money to buy cheese and an icecream")
