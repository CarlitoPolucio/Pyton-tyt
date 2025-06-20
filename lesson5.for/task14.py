time = int(input("wake up time: "))

kcal_counter = 0
water = 0

while time <= 23:
    kcal = int(input("kcal: "))
    water += 1
    kcal_counter += kcal
    time += 3
print(f"water is {water} liters", f"\nkcal: {kcal_counter}")
