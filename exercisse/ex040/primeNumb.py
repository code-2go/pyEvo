number = int(input('Enter an number: '))
divisor = 0 
for counter in range(number, 0, -1):
    if number%counter == 0:
        divisor = divisor + 1
if divisor == 2:
    print('The number {} is prime'.format(number))
else:
    print('The number {} ins\'t prime'.format(number))
