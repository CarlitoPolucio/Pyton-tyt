from math import log2, ceil

num1 = int(input("num1: "))
num2 = int(input("num2: "))

secret = int(input("secret: "))
count = ceil(log2(num2 - num1 + 1))
guess = (num1 + num2) // 2


while guess != secret:
    if secret > guess:
        num1 = guess
        guess = (guess + num2) // 2
        print(guess)
    elif secret < guess:
        num2 = guess
        guess = (guess + num1) // 2
        print(guess)

