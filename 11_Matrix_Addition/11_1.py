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

myList = [([0] * 3) for i in range(3)]

for i in range(3):
    for j in range(3):
        myList[i][j] = X[i][j] + Y[i][j]

print myList
