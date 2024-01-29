from random import randint
list10 = []
for cnt in range(0, 10):
    list10.append(randint(0, 10))
print(list10)
if 10 in list10:
    print(f'The number 10 is in position: ', end='')
    for pos, check in enumerate(list10):
        if check == 10:
            print(pos, end=' ')
else:
    print('There isn\'t number 10 on the list')
