temp = int(input("Enter the temp: "))

distance = 0
while temp > 15:
    distance += 20
    print(f"distance is {distance}")
    temp -= 2
    if temp <= 15:
        break
    elif temp >15:
        distance += 10

# Оптимизация

# temp = int(input("Enter the temp: "))
#
# distance = 0
# while temp > 15:
#     distance += 20
#     print(f"distance is {distance}")
#     temp -= 2
#     if temp <= 15:
#         break
#     distance += 10


