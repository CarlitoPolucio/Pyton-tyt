user_input = input("enter the text: ")

count = 0
checker = 0

for word in user_input:
    count += 1
    if checker < count:
        checker = count
    if word == " ":
        count = 0
        checker -= 1

print(checker)