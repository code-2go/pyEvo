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
        evenList.append(cnt)
    elif cnt % 2 == 1:
        oddList.append(cnt)
print(f'The complet list is {nList}\n')
print(f'The even list is {sorted(evenList)}\n')
print(f'The odd list is {sorted(oddList)}')