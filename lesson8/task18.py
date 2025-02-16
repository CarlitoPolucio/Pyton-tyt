def converter(chatles):
    CR = chatles / 2200
    ships = CR // 0.5
    return f"You have {CR} credits. It is {int(ships)} ships."

user_input = int(input("Enter the amount of chatles: "))
print(converter(user_input))
