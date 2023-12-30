# city = input('Enter the city where you live: ').strip().upper()
# print('SANTO' in city.split()[0])

# name = input('Enter your complete name: ').strip()
# print('SILVA' in name.upper())

name = input('Enter your complete name: ').title()
print('First name: {} \nLast name: {}'.format(name.split()[0], name.split()[len(name.split())-1]))
