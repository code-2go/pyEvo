# Create a program with a list and two function: lottery() and sumEven().
# The first will provide 5 random numbers and record them in the list.
# The second function will display the sum of all even numbers drawn. 
from random import randint


def drawn():
    for cnt in range(0, 6):
        n = randint(0, 61)
        if n not in lottery:
            lottery.append(n)
        else:
            while n in lottery:
                n = randint(0, 61)
            lottery.append(n)
    return sorted(lottery)


def even():
    sum = 0
    for cnt in lottery:
        if cnt % 2 == 0:
            sum += cnt
    return sum


lottery = []
print(f'These are the lottery numbers drawn: {drawn()}')
print(f'For the numbers drawn, this is the sum of all the even numbers: {even()}')
