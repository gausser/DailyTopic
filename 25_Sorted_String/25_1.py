# all the char change to lowercase, then sort the string
def SortString(string):
    LowerString = string.lower()
    StrList = list(LowerString)
    StrList.sort()
    LowerString = "".join(StrList)
    
    return LowerString

# Find the uppercase in the original string;
# Conversion the lowercase to uppercase in the new string if it is uppercase in the original string    
def MainFunction(string):
    # sort the original string
    NewString = SortString(string)

    for i in range(len(string)):
        if True == string[i].isupper():
            tmp = string[i].lower()
            index = NewString.find(tmp)
            NewString = NewString.replace(NewString[index], NewString[index].upper(), 1)
    return NewString

OriginalString = 'eaAsqWAwaeqwerQwqRRRRRRRRRRRertwer'
print MainFunction(OriginalString)