reverse_timer = int(input("Enter the time: "))

countdown = range(reverse_timer, 0, -1)
counter = reverse_timer

for second in countdown:
    print(second)
    counter -= 1
    user_choice = int(input("Is the food ready(1) or not(2)?: "))
    if user_choice == 1:
        break
print(f"Food is ready. Time remain: {counter}")
