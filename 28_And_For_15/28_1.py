
lst = []
for i in range(1, 10):
    for j in range(i, 10):
        for k in range(j , 10):
          # set can avoid duplication
          if ((i + j + k == 15) and (len(set([i, j, k])) == 3)):
              lst = lst.append([i, j, k])
for i in lst:
    print i