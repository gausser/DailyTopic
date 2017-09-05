count = 0
print "The number is: "
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5): 
            if (i != j) and (j != k) and (i != k):
                count += 1
                print i * 100 + j * 10 + k,
                if count % 4 == 0:
                    print             
print "The count of number is:", count            
