from random import choice
from time import sleep
plays = ('Scissor', 'Rocks', 'Paper')
playerChoice = int(input('Chose one:\n[1] Scissors\n[2] Rock\n[3] Paper\n'))
if playerChoice == 1:
    playerChoice = plays[0]
elif playerChoice == 2:
    playerChoice = plays[1]
elif playerChoice == 3:
    playerChoice = plays[2]
if (playerChoice == plays[0]) or (playerChoice == plays[1]) or (playerChoice == plays[2]):
    print('RO')
    sleep(.3)
    print('   SHAM')
    sleep(.3)
    print('        BO!!!')
    sleep(.3)
    pcPlay = (choice(plays[0:2]))
    print('You - {} Vs {} - PC'.format(playerChoice, pcPlay))
    if (pcPlay == plays[0]) and (playerChoice == plays[2]):
        print('You LOSE! Scissors wins the paper')
    elif (pcPlay == plays[0]) and (playerChoice == plays[1]):
        print('You WIN! Rock wins the scissors')
    elif (pcPlay == plays[1]) and (playerChoice == plays[2]):
        print('You WIN! Paper wins the rock')
    elif (pcPlay == plays[1]) and (playerChoice == plays[0]):
        print('You LOSE! Rock wins the scissors')
    elif (pcPlay == plays[2]) and (playerChoice == plays[0]):
        print ('You WIN! Scissors wins the paper')
    elif (pcPlay == plays[2]) and (playerChoice == plays[1]):
        print ('You LOSE! Paper wins the rock')
    elif (pcPlay == playerChoice):
        print('DRAW!')
else:
    print('Wrong choice!')
