num = (int(input('Enter the first number: ')), int(input('Enter the second number: ')), int(input('Enter the thrid number: ')), int(input('Enter the fourth number: ')))
if 9 in num:
    # cnt9 = 0
    # for cnt in num:
    #     if cnt == 9:
    #         cnt9 += 1
    # print(f'There are {cnt9} number(s) 9 in the tuple')
    print(f'There are {num.count(9)} number(s) 9 n the tuple')
else:
    print('There aren\'t numbers 9 in the tuple')
if 3 in num:
    # for cnt in num:
    #     if cnt == 3:
    #         print(f'The first number 3 is in {(num.index(cnt)+1)}o position')
    #         break   
    print(f'The first number 3 is in {(num.index(3)+1)}o position')
else: 
    print('There aren\'t number 3 in the tuple')
check = 0
for cnt in num:
    if cnt % 2 == 0:
        check = 1
if check == 1:
    print('The even number(s) in tuple is (are):', end=' ')
    for cnt in num:
        if cnt % 2 == 0:
            print(cnt, end=' ')
else:
    print('This tuple only contains odd numbers')
