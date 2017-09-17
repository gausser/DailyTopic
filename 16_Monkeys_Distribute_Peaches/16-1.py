from __future__ import division  

last = 4    #The quantity of Peaches is at least 4 after The 5th Monkey take
while True:
    tmp = last  #Every time "last" start
    for i in range(5):
        tmp = tmp / 4 * 5 + 1   # Recursive Formula between the monkey take the quantity of peaches 
        #print tmp
        if tmp  % 4 != 0:   # The quantity of peaches left every time is a multiple of four
            break
    else:
        print "The total is: ", tmp  # Print the final Quantity
        break

    last = last + 1   # one by one 