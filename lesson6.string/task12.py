text = input("text: ")

count = 0

for letter in text:
    count += 1

poz = 0
neg = 0

while poz + neg * -1 != count:
    print(text[poz], end="")
    poz += 1
    if poz + neg * -1 == count:
        break
    neg -= 1
    print(text[neg], end="")
