people = list(range(1, 11))
step = 3
to_remove = []
count = 0
while len(people) != 1:
    for man in people:
        count += 1
        if count % step == 0:
            to_remove.append(man)
    [people.remove(x) for x in to_remove]
    to_remove = []

print(people)