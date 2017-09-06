for number in range(-100, 10000):
    a = (number + 100) ** 0.5
    b = (number + 268) ** 0.5
    #if (a % 1 == 0) and (b % 1 == 0):
    #if (not a % 1) and (not b % 1):
    if a.is_integer() == True and b.is_integer() == True:
        print number
        
    