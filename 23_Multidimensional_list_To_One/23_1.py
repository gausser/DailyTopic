
new_list = []
def Multi_List_Turn_One_List(a):

    if len(a) == 0:
        new_list = []

    for i in range(len(a)):
        if type(a[i]) != list:
            new_list.append(a[i])
        else:
            Multi_List_Turn_One_List(a[i])

list1 = [1, [2], [3, 4], [[5, 6], 7], [8, [[9, [10], 11], 12], 13]]

Multi_List_Turn_One_List(list1)
print new_list
    
