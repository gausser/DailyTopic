
# For import permutations
import itertools
import numpy

s = range(1, 10)
# lst is full arrangement of [1 - 10]: 9!
lst = list(itertools.permutations(s, 9))
count = 0

for FullArrange in lst:
    if FullArrange[0] + FullArrange[3] + FullArrange[6] == 15 and \
       FullArrange[1] + FullArrange[4] + FullArrange[7] == 15 and \
       FullArrange[2] + FullArrange[5] + FullArrange[8] == 15 and \
       FullArrange[0] + FullArrange[4] + FullArrange[8] == 15 and \
       FullArrange[2] + FullArrange[4] + FullArrange[6] == 15 and \
       FullArrange[0] + FullArrange[1] + FullArrange[2] == 15 and \
       FullArrange[3] + FullArrange[4] + FullArrange[5] == 15 and \
       FullArrange[6] + FullArrange[7] + FullArrange[8] == 15:
       TmpArray = numpy.array(FullArrange)
       TmpArray = TmpArray.reshape((3, 3)) # Change the shape of the array: 3 rows and 3 columns
       count += 1
       print "#" * 20
       print FullArrange
       print TmpArray
       
print "The total number is:", count