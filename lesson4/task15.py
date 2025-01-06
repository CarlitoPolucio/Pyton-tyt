riddle = int(input("num: "))
count1 = 0
number = 100
if riddle <= 25:
    while number != riddle:
        number //= 2
        if number > riddle:
            continue
        elif number < riddle:
            number = number + number // 2
        else:
            print("Win")
            break
if riddle > 25 or riddle <= 50:
    while number != riddle:

if riddle > 50 or riddle <= 75:
    while number != riddle:

if riddle > 75 or riddle <= 100
    while number != riddle:


