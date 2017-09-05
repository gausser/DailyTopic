list_number = []

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                list_number.append(i * 100 + j * 10 + k)
                
print "The number is: ", list_number
print "The count of number is: ", len(list_number) 