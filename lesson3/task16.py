first_coin = int(input("Enter the weight of the first coin: "))
second_coin = int(input("Enter the weight of the second coin: "))
third_coin = int(input("Enter the weight of the third coin: "))

if third_coin != first_coin == second_coin != third_coin:
    print("Third coin is fake.")
elif first_coin != second_coin == third_coin != first_coin:
    print("First coin is fake.")
if third_coin != second_coin != first_coin:
    print("Second coin is fake.")
elif third_coin == second_coin == first_coin:
    print("They are the same. There is no fake. Or maybe they are all fakes?")