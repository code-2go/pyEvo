n = float(input('Enter your current salary $'))
#nIncrease = n*1.15
#print('CONGRATS! Your new salary is ${:.2f}'.format(nIncrease))
#===============================================================
#Part 2
if n>1250:
    nIncrease = n*1.1
else:
    nIncrease = n*1.15
print('CONGRATS! Your new salary is ${:.2f}'.format(nIncrease))
