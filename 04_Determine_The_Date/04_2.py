days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

'''judge is leap year'''
def leapyear(n):
    if ((n % 4 == 0) and (n % 100 != 0)) or (n % 400 == 0):
        return True
    else:
        return False
    
year, month, day = [int(x) for x in raw_input("Enter year/month/day: ").split('/')]
days2 = sum(days[:month - 1]) + day 

if (leapyear(year) == True) and month > 2:
    days2 += 1

print "The sum day is: ", days2   


