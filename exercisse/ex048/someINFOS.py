repeat = 1
greater = lower = sum = cnt =  0
while not(repeat != 1):
    n = int(input('Enter an integer: '))
    if (lower == 0) and (greater == 0):
        lower = greater = n
    elif lower > n:
        lower = n
    elif greater < n:
        greater = n
    cnt += 1
    sum += n
    ma = sum/cnt
    repeat = int(input('Repeat? \n[1] YES or [2] NO\n'))
    while not(repeat == 1) and not(repeat == 2):
        repeat = int(input('Wrong type. Please do you wanna repeat? \n[1] YES or [2] NO]\n'))
if repeat == 2:
    print('The smallest number is {} and largest number is {}. The arithmetic ratio of all the numbers entered is {:.1f}'.format(lower, greater,ma))
    print('\nThank You!')
