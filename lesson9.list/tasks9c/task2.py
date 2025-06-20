X = 1.05
Y = 1.1
GOODS = [21.99, 29.99, 55.34, 66.50, 14.88]
print(round(sum([price * X for price in GOODS]), 2), round(sum([price * Y for price in GOODS]), 2))