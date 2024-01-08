import datetime
born = int(input('Insert the year you were born: '))
year = datetime.date.today().year
age = year-born
if age >= 18:
    print('You should do military service right now!')
elif age == 17:
    print('Register to the next year military service.')
elif age < 17:
    print("Don't worry. You will olny register in {} years.".format(18-age))
