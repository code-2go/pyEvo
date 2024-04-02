# Create a program with a function that takes the year of birth of a user and returns a string value 
# that's displayed if the user is eligible to vote, insn't eligible to vote or if voting is optional.


def check(n):
    from datetime import date
    age = (date.today().year) - n
    if age >= 18 and age < 65:
        return 'You are eligible to vote'
    elif age < 18:
        return 'Sorry, you aren\'t eligible to vote'
    elif age >= 65:
        return 'Your vote is optional'


year = int(input('For check your voting situation, please enter your birth year: '))
print(check(year))
