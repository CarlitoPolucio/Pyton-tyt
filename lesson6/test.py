user_input = input("Enter the word: ")

count = -1
second_part = ""

for letter in user_input:
    count += 1
    if count % 2 > 0:
        second_part = letter + second_part
        continue
    print(letter, end="")
print(second_part, end="")




















