size_list = input("size list (space): ").split()
legs = input("legs list (space): ").split()
count = 0
for x in size_list:
    if x in legs:
        legs.remove(x)
        count += 1

print(count)
