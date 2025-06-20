user_input = input("enter num: ")

count = 0

for num in user_input:
    if num == " ":
        continue
    elif int(num) > 5:
        count += 1

print(count)