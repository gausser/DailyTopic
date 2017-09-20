list1 = [1, [2], [3, 4], [[5, 6], 7], [8, [[9, [10], 11], 12], 13]]

print([int(i.strip(' []')) for i in str(list1).split(',')]) 
