
def sum_num(n):
    result = 0
    c = 1
    num_list = list(range(1, n + 1))

    while len(num_list) > 0:
        tmp = 1
        for i in range(c):
            if len(num_list) > 0:
                tmp = tmp * num_list.pop(0)
        result = result + tmp
        c = c + 1
    else:
        return result

number = int(raw_input("Please input the number:"))
a = sum_num(number)
print a

