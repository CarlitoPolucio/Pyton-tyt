value = int(input("How many cards: "))
cards = range(1, value + 1)
check = sum(cards)
checker = 0

for card in cards:
    if card == value:
        break
    number = int(input("enter the num: "))
    checker = number + checker
answer = check - checker
print(f"{answer} is lost")
