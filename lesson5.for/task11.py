needed_hour = int(input("Enter time to end: "))
shit = 1
timer = 0

while needed_hour != timer:
    shit *= 2
    timer += 3
    time_remain = needed_hour - timer
    print(f"Time remaining: {time_remain}", f"\nHours passed: {timer}", f"\nShit is: {shit}")
    input("Enter conclusion: ")
