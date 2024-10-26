counter = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen','sixteen', 'seventeen', 'eighteen', 'niteen', 'twenty')
num = int(input('Choose a number from 1 to 20: '))
while num < 1 or num > 20:
    num = int(input('The number isn\'t valid. Try again!\nChoose a number from 1 to 20 : '))
print((counter[num-1]).title())