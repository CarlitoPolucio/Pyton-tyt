width = int(input("Enter the width: "))
height = int(input("Enter the height: "))

width -= 2

for height_sign in range(1, height + 1):
    if height_sign == 1 or height_sign == height:
        print("|", "-" * width, "|", sep="")
    else:
        print("|", " " * width, "|", sep="")

