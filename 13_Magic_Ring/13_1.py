def Take_Mold(n):
    if n >= 100:
        n = n % 100
    return n

def Magic_Ring(ring, loop):
    number = 1
    count = len(ring)
    
    while number <= loop:
        first = ring[0]
        
        for i in range(count - 1):
            ring[i] = Take_Mold(ring[i] + ring[i + 1])

        ring[count - 1] = Take_Mold(ring[count - 1] + first)
        number += 1
        
    return ring


ring = [1, 2, 3, 4, 5, 65]
print ring
print
print Magic_Ring(ring, 200000)