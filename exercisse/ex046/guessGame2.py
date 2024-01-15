from random import randint
npc = randint(0, 100)
player = int(input('Choice an integer: '))
play = 0
while player != npc:
    if player < npc:
        print('To lower')
    elif player > npc:
        print('To higher')
    play += 1
    player = int(input('Choice an integer: '))
    if player == npc:
        print('THAT\'S IT! You WIN!!!')
print('To guess the number, you needed {} plays'.format(play+1))
    