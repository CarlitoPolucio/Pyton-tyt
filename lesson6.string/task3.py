text = input("Enter the text: ")

count = 0

for letter in text:
    if letter.lower() == "ы" :
        count += 1

print(count)


