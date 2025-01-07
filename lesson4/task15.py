# secret = int(input("num: "))
#
# num = 0
# count = 0
#
# if secret >= 50:
#     count += 1
#     if secret >= 75:
#         count += 1
#         if secret >= 88:
#             count += 1
#             num = 88
#             while num != secret:
#                 count += 1
#                 num += 1
#         else:
#             count += 1
#             while num != secret:
#                 count += 1
#                 num += 1
#     elif secret < 75:
#         count += 1
#         num = 64
#         if secret <= 63:
#             num = 50
#             count += 1
#             while num != secret:
#                 count += 1
#                 num += 1
#         else:
#             count += 1
#             while num != secret:
#                 count += 1
#                 num += 1
#
# if secret < 50:
#     count += 1
#     if secret <= 25:
#         count += 1
#         while num != secret:
#             count += 1
#             num += 1
#     else:
#         count += 1
#         num = 26
#         while num != secret:
#             count += 1
#             num += 1


# print(count)
from math import log2, ceil

left, right = 1, 100
secret = int(input(f"Enter your secret number at {left} to {right}: "))
guess = right // 2
count = ceil(log2(right))
while left < right:
    count -= 1
    if count == 0:
        print("You're making a fool out of me.")
        break
    if secret == guess:
        print(f"Your secret is {secret}")
        break
    user_help = input(f"Your number more(1) or less(2) than {guess}? ")
    if user_help == "1":
        left = guess
    elif user_help == "2":
        right = guess
    guess = (left + right) // 2
else:
    print("Your number out of range.")
