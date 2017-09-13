def Monkey_Eat_Peach(n):
    if n == 1: # The last day
        return 1
    else:
        return (Monkey_Eat_Peach(n - 1) + 1) * 2

print Monkey_Eat_Peach(10)
