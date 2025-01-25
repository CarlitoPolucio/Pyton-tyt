user_input = input(" Enter 10 cow places. a - free, b - occupied: ")

milk = 0
milk_production = 0

for letter in user_input:
    milk += 2
    if letter == "b":
        milk_production += milk

print(milk_production, "l.")



