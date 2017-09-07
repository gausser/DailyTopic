
profit = int(raw_input("Enter your profit: "))

if profit <= 100000:
    bonus = profit * 0.1
elif profit < 200000:
    bonus = (profit - 100000) * 0.075 + 100000 
elif profit < 400000:
    bonus = (profit - 200000) * 0.05 + 100000 * (0.1 + 0.075)
elif profit < 600000:
    bonus = (profit - 400000) * 0.03 + 200000 * 0.05 + 100000 * (0.1 + 0.075)
elif profit < 1000000:
    bonus = (profit - 600000) * 0.015 + 200000 * (0.05 + 0.03) + 100000 * (0.1 + 0.075)
else:
    bonus = (profit - 1000000) * 0.01 + 400000 * 0.015 + 200000 * (0.05 + 0.03) + 100000 * (0.1 + 0.075)
    
print "Your bonus is: ", bonus    