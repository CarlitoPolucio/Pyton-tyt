exp = int(input("Enter exp: "))

if exp < 1000:
    print("yr levul is 1")
elif 2500 > exp >= 1000:
    print("yr levul is 2")

if 5000 > exp >= 2500:
    print("yr levul is 3")
elif exp >= 5000:
    print("yr levul is 4")

# Оптимизация

# exp = int(input("Enter exp: "))
# level = 1
# if 1000 <= exp < 2500:
#     level = 2
# elif 2500 <= exp < 5000:
#     level = 3
# elif 5000 <= exp:
#     level = 4
#
# print(f"yr levul is {level}")
