
from __future__ import division  

def Fun_Main(n):
    sum_value= 0

    for i in range(n, 0, -2):
        sum_value = sum_value + 1 / i

    return sum_value

result = Fun_Main(8000)
print result
