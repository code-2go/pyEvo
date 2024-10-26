import datetime
born = int(input('Insert the year you were born: '))
gender = int(input('Select your biological genre\n [1] - Male\n [2] - Female\n'))
year = datetime.date.today().year
age = year-born
if gender == 1:
    if age >= 18:
        print('You should do military service right now!')
    elif age == 17:
        print('Register to the next year military service.')
    elif age < 17:
        print("Don't worry. You will olny register in {} years.".format(18-age))
else:
    print("Don't worry, you're a girl. Girls don't need to register for military service.")
