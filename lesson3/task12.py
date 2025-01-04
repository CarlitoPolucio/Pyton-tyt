# Переделай эту задачу, множество условий задачи не выполнено

dublons = int(input("Enter the amount of dublons: "))

SEMENS_SWORD_PRICE = 55000
purchase = dublons - SEMENS_SWORD_PRICE
discount_purchase = dublons - SEMENS_SWORD_PRICE + 1000

if 0 <= dublons - SEMENS_SWORD_PRICE < 5000:
    print(f"Purchase completed, you got a bonus of 1000 points. Your balance is {discount_purchase} points.")
elif dublons > SEMENS_SWORD_PRICE:
    print(f"Purchase completed. Your balance is {purchase} points.")
else:
    print(f"You don't have enough points (55000). You already have {dublons} points.")
