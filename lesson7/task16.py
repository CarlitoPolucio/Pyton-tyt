
road = 1
empty_space = 20


for y in range(0, 20):
    empty_space -= 1
    road += 1
    if y == 10:
        print("-" * 51)
        continue
    print(" " * empty_space, "/", " " * road ,"|", " " * road, "\\", " " * empty_space)
