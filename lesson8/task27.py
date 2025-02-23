def currency(eu):
    ru = eu * 1.25 * 60.87
    return round(ru, 2)


user_input = float(input("Enter the price: "))
print(currency(user_input))
