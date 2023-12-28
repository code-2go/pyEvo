
name = input('Enter your name: ')
print(name.upper())
print(name.lower())
print('Your complete name has {} letters.'.format(len(''.join(name.split()))))
print('Your first name has {} letters.'.format(len(name.split()[0])))
