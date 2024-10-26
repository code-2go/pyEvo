'''Make a dice game program for four players. The result of the moves should be recorded in the dictionary. At the end, sort the registers for display the players' results'''
from random import randint
from time import sleep
from operator import itemgetter
players = {}
lowest = highest = 0
for cnt in range(0, 4):
    players[f'player {cnt+1}'] = randint(1, 6)
for keys, values in players.items():
    print(f'{keys} moves: {values}')
    sleep(.5)
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
print('-='*17)
print(('Players Ranking').center(35))
print('=-'*17)
for cnt in range(0, len(players)):
    print(f'Position {cnt+1} is {ranking[cnt][0]} who moves {ranking[cnt][1]}') 
    sleep(0.5)