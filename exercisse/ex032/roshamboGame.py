from random import choice, shuffle
from time import sleep
scissors = 'Scissors'
rock = 'Rock'
paper = 'Paper'
playerChoice = int(input('Chose one:\n[1] Scissors\n[2] Rock\n[3] Paper\n'))
if playerChoice == 1:
    playerChoice = scissors
elif playerChoice == 2:
    playerChoice = rock
elif playerChoice == 3:
    playerChoice = paper
pcPlay = (choice([scissors, rock, paper]))
print('You {} Vs {} PC'.format(playerChoice, pcPlay))
print('R O S H A M B O')
sleep(1.5)
if (pcPlay == scissors) and (playerChoice == paper):
    print('You LOSE!. Scissors wins the paper')
elif (pcPlay == scissors) and (playerChoice == rock):
    print('You WIN! Rock wins the scissors')
elif (pcPlay == rock) and (playerChoice == paper):
    print('You WIN! Paper wins the rock')
elif (pcPlay == rock) and (playerChoice == scissors):
    print('You LOSE! Rock wins the scissors')
elif (pcPlay == paper) and (playerChoice == scissors):
    print ('You WIN! Scissors wins the paper')
elif (pcPlay == paper) and (playerChoice == rock):
    print ('You LOSE! Paper wins the rock')
elif (pcPlay == playerChoice):
    print('DRAW!')
