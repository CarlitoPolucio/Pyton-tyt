text = input("text: ")
user_answer = input("do you want decypher this text? Y or N: ")

count = -1

for letter in text:
    count += 1

step = 2
words = range(0, count + 1, step)

poz = 0
neg = 0

if count % 2 == 0:
    count += 1

neg -= 1
if user_answer == "N":
    while poz < count:
        print(text[poz], end="")
        poz += 2
    while neg * -1 <= count:
        print(text[neg], end="")
        neg -= 2




