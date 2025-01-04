profit = int(input("Enter the profit: "))

if profit < 0:
    print("dude")
else:
    if profit <= 10000:
        profit *= 0.13
    elif 50000 > profit > 10000:
        profit *= 0.2
    else: profit *= 0.3
    print(f"Your tax is {profit} ")

