table = int(input("Enter the price of the table: "))
chair = int(input("Enter the price of the chair: "))
sofa = int(input("Enter the price of the sofa: "))

price_sum = table + chair + sofa
discount_price = price_sum - (price_sum * 0.1)

if price_sum >= 10000:
    print(f"For payment: {discount_price}$")
else:
    print(f"For payment: {price_sum}$")

