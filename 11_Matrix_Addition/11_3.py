X = [
     [12,7,3],
     [4,5,6],
     [7,8,9]
    ]

Y = [
     [5,8,1],
     [6,7,3],
     [4,5,9]
    ]

myList = [i + j for i, j in zip(sum(X, []), sum(Y, []))]

myList = [myList[0:3], myList[3:6], myList[6:9]]
print myList
          
