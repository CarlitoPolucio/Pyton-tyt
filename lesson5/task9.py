# value = int(input("How many cards: "))
# cards = range(1, value + 1)
# check = sum(cards)
# checker = 0
#
# for card in cards:
#     if card == value:
#         break
#     number = int(input("enter the num: "))
#     checker = number + checker
# answer = check - checker
# print(f"{answer} is lost")

# Оптимизация и полировка
value = int(input("How many cards: "))
total_cards_sum = value
current_cards_sum = 0

for card_num in range(1, value):
    num = int(input("enter the num: "))
    current_cards_sum += num
    total_cards_sum += card_num
answer = total_cards_sum - current_cards_sum
print(f"{answer} is lost")
