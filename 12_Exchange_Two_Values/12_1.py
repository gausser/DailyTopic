list1 = [1, 2, 3, 4, 5, -1, 0, 19, 7, 8, 9]

max_index = list1.index(max(list1))
min_index = list1.index(min(list1))

list1[0], list1[max_index] = list1[max_index], list1[0]

list1[-1], list1[min_index] = list1[min_index], list1[-1]

print list1