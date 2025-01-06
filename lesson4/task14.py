
riddle = int(input("num: "))
count = 0
while True:
    count += 1
    num = int(input("num: "))
    if num == riddle:
        print(f"ok. you made {count} attempts.")
        break
    elif num > riddle:
        print("Your number is higher")
    else:
        print("Your number is less")

