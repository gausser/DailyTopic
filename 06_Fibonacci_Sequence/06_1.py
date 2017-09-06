
def CalculationFibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return CalculationFibonacci(n - 1) + CalculationFibonacci(n - 2)

n = int(raw_input("Enter the Fibonacci Number: "))
for i in range(n):
    print CalculationFibonacci(i),
