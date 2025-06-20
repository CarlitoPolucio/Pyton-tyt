weight_one = int(input("Enter the first indication: "))
weight_two = int(input("Enter the second indication: "))

if weight_two == weight_one:
    print("same weight")
elif weight_two > weight_one:
    print(" Second indication weighs more")
else:
    print("First one weighs more")