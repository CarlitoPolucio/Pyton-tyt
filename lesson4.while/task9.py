number1 = int(input("Enter the number: "))
while True:
    number = int(input("Enter the number: "))
    if number == number1:
        var = (input("Do you wanna continue?(Y/N)"))
        if var == "N":
            break
    number1 = int(input("Enter the number: "))
    if number == number1:
        var = (input("Do you wanna continue?(Y/N)"))
        if var == "N":
            break


