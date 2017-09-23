from __future__ import division

# Get a and b 's the Maximum common divisor
def Max_Common_Divisor(a, b):
    while b != 0:
        c = a % b 
        a = b 
        b = c
    return a  # a is max common divisor

# Get a and b's the least common multiple
def Min_Common_Multiple(a, b):
    return a * b / a 

# Fractional Addition
# a is the first fraction's molecular, b is the first fraction's Denominator
# c is the second fraction's molecular, d is the second fraction's Denominator
# return the molecular and Denominator of Fraction_Add_Fraction's Add and Minus
def Add_Minus_Of_Fraction_Fraction(a, b, c, d):
    list = []
    New_Multiple = Min_Common_Multiple(b, d)
    b_Business = New_Multiple / b 
    d_Business = New_Multiple / d 
    
    a = a * b_Business
    c = c * d_Business
    
    # Get Add of Fractions
    Add_Molecular = a + c
    Add_Divisor = Max_Common_Divisor(New_Multiple, Add_Molecular)
    list.append(int(Add_Molecular / Add_Divisor))
    list.append(int(New_Multiple / Add_Divisor))
    
    # Get Minus of Fractions 
    Minus_Molecular = a - c 
    Minus_Divisor = Max_Common_Divisor(New_Multiple, Minus_Molecular)
    list.append(int(Minus_Molecular / Minus_Divisor))
    list.append(int(New_Multiple / Minus_Divisor))
    
    print "%d/%d + %d/%d = %d/%d" % (a, b, c, d, list[0], list[1])
    print "%d/%d - %d/%d = %d/%d" % (a, b, c, d, list[2], list[3])
