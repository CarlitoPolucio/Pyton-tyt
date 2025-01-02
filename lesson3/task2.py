account = int(input("Enter account balance: "))

if account >= 100:
    operation = account - 100
    print(f"Purchase completed. Your account balance is {operation}$. Have a good day!")
else:
    print("Purchase error. Not enough funds in the account. Have a good day!")

