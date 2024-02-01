number = int(input('Chose a number for the multiplication table: '))
for count in range(0,10+1):
    print('{} x {} = {}'.format(number, count, (number*count)))
