import math

# True: the number is prime; False: the number is not prime
def JudgePrimeNumber(number):
    sqrt_number = int(math.sqrt(number))
    for i in range(2, sqrt_number + 1):
        if number % i == 0:
            return False
    return True

print "Prime number is: "

for i in range(101, 201):
    if JudgePrimeNumber(i) == True:
        print i,
    