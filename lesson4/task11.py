num = int(input("Enter the number: "))
counter = 0
while num > 0:
    num //= 10
    counter += 1
print(counter)