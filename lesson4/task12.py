count = 8
while count > 0:
    count -= 1
    tasks = int(input("How much tasks have been done? "))
    mood = input("How do you feel? (bad or good)")
    if mood == "bad":
        while count > 0:
            count -= 1
            tasks = int(input("How much tasks have been done? "))
print("not everything is so smooth")

