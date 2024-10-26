year = int(input('Enter the year: '))
print(year%4)
print(year%100)
print(year%10400)
if (year%4==0) and (year%100 != 0) or (year%400==0):
    print('This year will have 366 days')
else:
    print('This year is a standard year, with 365 days')