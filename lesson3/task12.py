user_balance = int(input("Enter the amount of dublons: "))

SEMENS_SWORD_PRICE = 55000
purchase = user_balance - SEMENS_SWORD_PRICE
discount_purchase = user_balance - SEMENS_SWORD_PRICE + 1000

if 0 <= user_balance - SEMENS_SWORD_PRICE < 5000:
    print(f"Purchase completed, you got a bonus of 1000 points. Your balance is {discount_purchase} points.")
elif user_balance > SEMENS_SWORD_PRICE:
    print(f"Purchase completed. Your balance is {purchase} points.")
else:
    print(f"You don't have enough points (55000). You already have {user_balance} points.")

# Оптимизация
# user_balance = int(input("Enter the amount of dublons: "))
#
# SEMENS_SWORD_PRICE = 55000
# BONUS = 1000
# BONUS_FACTOR = 5000
#
# if SEMENS_SWORD_PRICE <= user_balance:
#     user_balance -= SEMENS_SWORD_PRICE
#     if user_balance < BONUS_FACTOR:
#         user_balance += BONUS
#         print(f"You got a bonus of {BONUS} points.")
#     print(f"Purchase completed")
# else:
#     print(f"You don't have enough points ({SEMENS_SWORD_PRICE}).")
#
# print(f"Account balance: {user_balance}")
