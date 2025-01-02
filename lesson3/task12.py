# Переделай эту задачу, множество условий задачи не выполнено

dublons = int(input("Enter the amount of dublons: "))

semens_sword_price = 55000
purchase = dublons - semens_sword_price
discount_purchase = dublons - semens_sword_price + 1000

if dublons > semens_sword_price + 5000:
    print(f"Purchase completed. Your balance is {purchase} points.")
elif 0 < purchase < 5000:
    print(f"Purchase completed, you got a bonus of 1000 points. Your balance is {discount_purchase} points.")
else:
    print(f"You don't have enough points (55000). You already have {dublons} points.")
