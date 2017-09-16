list1 = [1, 2, 4, 5, 6, 7, 8, 9, 10, 12, 25]

n = 2 % len(list1)
while len(list1) > 1:
    list1.pop(n)
    n = (n + 2) % len(list1)
print('list1 %d'%list1[0])


