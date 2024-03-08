# Create a program with a function that takes the year of birth of a user and returns a string value 
# that's displayed if the user is eligible to vote, insn't eligible to vote or if voting is optional.


def check(n):
    age = (date.today().year) - n
    if age >= 18 and age < 65:
        return 'yes'
    elif age < 18:
        return 'no'
    elif age >= 65:
        return 'optional'


from datetime import date
year = int(input('For check your voting situation, please enter your birth year: '))
if check(year) == 'yes':
    print('You are eligible to vote')
elif check(year) == 'no':
    print('Sorry, you aren\'t eligible to vote')
elif check(year) == 'optional':
    print('Your vote is optional')
