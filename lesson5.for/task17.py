food_range = range(96, 1, -4)
print("information about remain food: ")

count = 0
for food in food_range:
    count += 1
    print(f"After {count} months: {food}kg food left")
print("After 25 months: food is out")