#library method
n = int(input('Enter a number and choose a converter base: '))
converter = int(input('[1] - Decimal to Binary \n[2] - Decimal to Octal \n[3] - Decimal to Hexadecimal\n'))
if converter == 1:
    print('The number {} converted to binary is {}.'.format(n, bin(n)[2:7]))
if converter == 2:
    print('The number {} converted to octal is {}.'.format(n, oct(n)[2:]))
if converter == 3:
    print('The number {} converter to hexagonal is {}.'.format(n, hex(n)[2:]))
if converter > 4:
    print('Invalid Option')
