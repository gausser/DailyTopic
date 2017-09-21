
Month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# If leap year, then return True; Or return False
def IsLeapYear(year):
    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        return True
    else:
        return False

def DateToNumber(date):
    year = date[0]
    month = date[1]
    day = date[2]
    months = sum(i * Month[i - 1] for i in range(1, month))
    
    # Get the days of Month
    if (True == IsLeapYear(year) and month > 1):
        months =  months + 1
    # Get the total days of the date 
    days = year * 365 + months + day

    return days

CurrentDate = [2014, 8, 18]
EntryDate = [2014, 8, 18]

print DateToNumber(CurrentDate) - DateToNumber(EntryDate)
