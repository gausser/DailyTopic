count = [1]
for i in range(2:11):
    count.append((count[i - 1] + 1) * 2)

print count
