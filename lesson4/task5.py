money = int(input("Enter your money: "))

while money < 3000:
    cube = int(input("Enter value:"))
    if cube == 3:
        print("Game over")
        break
    elif cube > 6 or cube < 1:
        print("incorrect value, enter from 1 to 6")
        continue
    money += 300
    print(f"your balance is {money}")
    if money >= 3000:
        print("limit reached")