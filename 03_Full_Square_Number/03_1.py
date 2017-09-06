import math

for number in range(-100,100000):
    # To determine whether a number is an int
    if (math.sqrt(number + 100) % 1 == 0) and (math.sqrt(number + 268) % 1 == 0):
        print number