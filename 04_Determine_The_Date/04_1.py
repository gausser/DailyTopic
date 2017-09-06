month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def DetermineDateOfYear(date):
    # To Determine the days of month
    IntOfMonth = int(date[4:6])
    for i in range(IntOfMonth - 1):
        DaysOfMonth = (i + 1) * month[i]
    # To Determine Leap year
    IntOfYear = int(date[0:4])
    if ((IntOfYear % 4 == 0) and (IntOfYear % 100 != 0)) or (IntOfYear % 400 == 0):
        TotalDays = DaysOfMonth + 1 + int(date[6:8])
    else: # Is not leap year
        TotalDays = DaysOfMonth + int(date[6:8])
    return TotalDays

DATE = raw_input("Enter the date(19700701):")
TotalDATE = DetermineDateOfYear(DATE)
print "The days of DATE is %d" % TotalDATE
        
        