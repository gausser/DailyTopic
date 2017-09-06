
first = int(raw_input("Enter the first value: "))
second = int(raw_input("Enter the second value: "))
third = int(raw_input("Enter the third value: "))
        
if first > second:
    first, second = second, first
if first > third: 
    first, third = third, first
print first  