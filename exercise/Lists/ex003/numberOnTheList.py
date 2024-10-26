numList = []
check = 'y'
while check != 'n':
    n = (int(input('Enter an integer: ')))
    if n in numList:
        print('That number is already on the list')
    else:
        numList.append(n)
        print('Value entered successfully!')
    check = str(input('Do you want enter another number?\nYes or No?\n')).strip().lower()[0]
numList.sort()
print(f'The final list is: {numList}')