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

myList = []

for i in range(3):
    myList.append([])
    for j in range(3):
        myList[i].append(X[i][j] + Y[i][j])

print myList
