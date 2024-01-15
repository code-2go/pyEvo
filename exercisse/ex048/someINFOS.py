from math import ceil
repeat = 1
greater =  0
lower = 0
sum = 0
cnt = 0
while not(repeat != 1):
    n = int(input('Enter an integer: '))
    if (lower == 0) and (greater == 0):
        lower = n
        greater = n
    elif lower > n:
        lower = n
    elif greater < n:
        greater = n
    cnt += 1
    sum += n
    ma = sum/cnt
    print('The lower number is {} and greater number is {}. The arithmetic ratio of all entered number is {}'.format(lower, greater, ceil(ma)))
    repeat = int(input('Repeat? \n[1] YES or [2] NO\n'))
    while not(repeat == 1) and not(repeat == 2):
        repeat = int(input('Wrong type. Please do you wanna repeat? \n[1] YES or [2] NO]\n'))
if repeat == 2:
    print('Thank You!')