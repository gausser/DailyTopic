

def Decomposing_Factor(number):
    Factor_List = []
    Min_Prime = 2
    
    while(number > 0):
        if 1 == number:
            Factor_List.append(number)
            print "1 decomposing factor is 1."
            break;
        if Min_Prime == number: # Description the decomposing_factor process ends
            Factor_List.append(number)
            break;
        else:
            if number % Min_Prime == 0:  # Divisible 2, this number is even
                number = number / Min_Prime
                Factor_List.append(Min_Prime)
            else:
                Min_Prime += 1

    return Factor_List
 
number = int(raw_input("Enter a Positive number: "))
Factor = []
result = str(number) + "="
if number > 0:
    Factor = Decomposing_Factor(number)
    for each in Factor:
        result = result + '%d*' % each
result = result[:-1]
print result         

   