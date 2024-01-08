from random import randint
from time import sleep
n = randint(0,5)
choose = int(input('Guess a number from 0 to 5: '))
print('Processing...')
sleep(3)
if choose == n:
    print('You WIN!')
else:
    print('Your worng. The number is {}'.format(n))