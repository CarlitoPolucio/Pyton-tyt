start_work = int(input("when did you start your work?: "))

work_day = 20 - start_work
activity_counter = 0
count = start_work
while count < 20:
    count += 1
    activity = int(input("sport time?: "))
    activity_counter += activity
    if activity_counter >= 45:
        print(f"you are good. activity is {activity_counter}, work day is {work_day} hours.")
        break
else:
    print(f"activity is {activity_counter}, work day is {work_day} hours")
