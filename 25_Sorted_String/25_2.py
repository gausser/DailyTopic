str1 = 'easqWAwaeq'

str2 = ''.join(sorted(list(str1), key = lambda x: ord(x) if ord(x) < 97 else ord(x) -31.5))

print(str2)
