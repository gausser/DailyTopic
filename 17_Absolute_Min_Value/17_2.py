int_list = [2, 3, 4, 5, 6, 7, 8, 9]

min = abs(int_list[0] - int_list[1])
for i in range(len(int_list)):
    for j in range(i):
        if abs(int_list[j] - int_list[i]) < min:
            min = abs(int_list[j] - int_list[i])
print min
