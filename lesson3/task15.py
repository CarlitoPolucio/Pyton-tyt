profit = int(input("Enter the profit: "))

if profit < 0:
    print("dude")
if 0 <= profit <= 10000:
    tax = profit * 0.13
    print(f"Your tax is {tax}$.")
elif 50000 >= profit > 10000:
    tax1 = profit * 0.2
    print(f"Your tax is {tax1}$")
if profit > 50000:
    tax3 = profit * 0.3
    print(f"Your tax is {tax3}$")

