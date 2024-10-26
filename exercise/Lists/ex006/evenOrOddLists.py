nList = []
evenList = []
oddList = []
while True:
    nList.append(int(input('Enter an number: ')))
    check = int(input('Continue?\n[1] Yes - [2] No\n'))
    if check == 2:
        break
for cnt in nList:
    if cnt % 2 == 0:
        if cnt in evenList:
            evenList.remove(cnt)
        evenList.append(cnt)
    if cnt % 2 == 1:
        if cnt in oddList:
            oddList.remove(cnt)
        oddList.append(cnt)
print(f'The complet list is {nList}')
print(f'The even list is {sorted(evenList)}')
print(f'The odd list is {sorted(oddList)}')
