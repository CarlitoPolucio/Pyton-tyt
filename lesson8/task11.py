x1 = int(input("Enter the X1: "))
y1 = int(input("Enter the y1: "))
x2 = int(input("Enter the X2: "))
y2 = int(input("Enter the Y2: "))

text = x1, y1, x2, y2

answer = max(text) - min(text)
print(answer)

