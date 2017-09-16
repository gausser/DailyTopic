people = [1, 2, 4, 5, 6, 7, 8, 9, 10, 12, 25]

count = 0
each = 0

while len(people) > 1:
    count += 1
    each = each + 1    
    if each > len(people):
        each = each % len(people)

    if count % 3 == 0:
        out = people.pop(each - 1)
        print out
        each = each - 1
        if each == len(people): each = 0
        count = 0
        if len(people) == 1:
            break

print people
