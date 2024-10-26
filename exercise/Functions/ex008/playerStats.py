# Create a function that receives two optional parameters: the player's name and the score of all matches. 
# The program displays the players' statistics even if some data is not recorded. ex: <unknown>; score: 10.


def playerStats(a='unknow', b=0):
    print(f'The soccer player: {a}, has scored {b} goals!')


name = str(input('Enter the player name: '))
goals = str(input('How much goals this player has scored? '))
if goals.isnumeric():
    goals = int(goals)
else:
    goals = 0
if name.strip() == '':
    playerStats(b = goals)
else:
    playerStats(name, goals)