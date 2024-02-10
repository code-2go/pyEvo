# Write an algorithm thats reads a group a,b. These are two positive integer variables. For each group, return MMC and MDC. 

a = int(input('Enter an integer: '))
b = int(input('Enter an integer: '))
cnt = 2
mmc = 1
mdc = 1 

while (a != 1) or (b != 1):
    if (a%cnt == 0) and (b%cnt == 0):  
        a = a//cnt
        b = b//cnt
        mmc = mmc*cnt  
        mdc = mdc*cnt
    elif (a%cnt == 0):
        a = a//cnt
        mmc = mmc*cnt
    elif (b%cnt == 0):
        b = b//cnt
        mmc = mmc*cnt
    else:
        cnt += 1
print(mmc)
print(mdc)

