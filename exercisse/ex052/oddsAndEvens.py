from random import randint
from time import sleep
cnt = 0
check = 0
while check != 2:
    while True:
        players_choice = int(input('\nChoose one: \n[1] For Odds [2] For Evens\n'))
        while players_choice !=1 and players_choice !=2:
            players_choice = int(input('\nChoose one: \n[1] For Odds [2] For Evens\n'))    
        str(players_choice)
        if players_choice == 1:
            players_choice = 'Odds'
            npc = 'Evens'
        else:
            players_choice = 'Evens'
            npc = 'Odds'
        players_move = int(input('Enter an integer number from 0 to 10: '))
        if players_move < 0 or players_move > 10:
            players_move = int(input('Try again! Enter an integer number from 0 to 10: ')) 
        npcs_move =  randint(0, 10)
        print(f'Your move was {players_move} x {npcs_move} for npc\'s move')
        print('Checking...')
        sleep(1)
        if ((players_move + npcs_move)%2 == 0) and (players_choice == 'Evens'):
            print('\nYou Win!')
            cnt += 1
        else:
            print('\nYou Lose!')
            break
    print(f'You had {cnt} wins')
    check = int(input('\nDo you wanna play again? \n[1] Yes or [2] No\n'))
print('\nThanks for playing!')
