def average():
    while True:
        a = int(input("Enter first num: "))
        b = int(input("Enter second num: "))
        if b < a:
            print("second number must be greater than first")
            continue
        return sum(range(a, b + 1)) / len(range(a, b + 1))

print(average())




