import math

for i in range(-100, 100000):
    # Must be converted to an integer
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if x * x == (i + 100) and y * y == (i + 268):
        print i