def positive():
    print("Positive")
def negative():
    print("Negative")

def test():
    user_input = int(input("Enter the num: "))
    if user_input > 0:
        positive()
    elif user_input < 0:
        negative()
    else:
        print("0")

test()