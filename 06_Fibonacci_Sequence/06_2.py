
def Fibonacci(n):
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    total = [0, 1]
    
    for i in range(2, n):
        total.append(total[i - 1] + total[i - 2])
    
    return total

print Fibonacci(2)
        