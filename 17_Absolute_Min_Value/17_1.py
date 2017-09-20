
list1 = [2, 3, 4, 5, 6]

list1.sort()
min_list = min(list1[i + 1] - list1[i] for i in range(len(list1) - 1))
print min_list

