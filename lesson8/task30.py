import math

a = 43535.354
c, d = math.modf(a)
c = math.floor(c * 10)
print(c)