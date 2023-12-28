# city = input('Enter the city where you live: ')
# print('santa' in city.split()[0])

# name = input('Enter your complete name: ')
# print('Silva' in name)

name = input('Enter your complete name: ')
print('First name: {} \nLast name: {}'.format(name.split()[0], name.split()[len(name.split())-1]))
