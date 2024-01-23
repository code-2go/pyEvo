standings = ('palmeiras', 'gremio', 'atletico mg', 'flamengo',
            'botafogo', 'bragantino', 'fluminense', 'atletico pr', 
            'internacional', 'fortaleza', 'sao paulo', 'cuiaba', 'corinthians', 'cruzeiro', 'vasco da gama', 'bahia', 'santos', 'goias', 'coritiba', 'america mg')

print('-' * 25)
print('First Five:\n')
for cnt in range(0, 5):
    print(f'{cnt+1}o place - {standings[cnt]}')
print('\nLast Five:\n')
for cnt in range(len(standings)-5, len(standings)):
    print(f'{standings[cnt]} is in {cnt+1}o place')
print('-' * 25)
print('\nSorted Standins:\n')
ordered = sorted(standings)
for cnt in range(0, len(standings)):
    print(ordered[cnt])
print('')
print('-' * 25)
select = str(input('\nEnter the team name to show its position: ')).strip().lower()
while select not in standings:
    print('\nTeam not found!')
    if select in 'vasco atletico america':
        print('\nTIPS: Enter a complete team name. Ex.: Vasco da Gama, Atletico PR, Atletico MG or America MG\n')
    select = str(input('Please try again: ')).strip().lower()   
print(f'\n{(select).title()} is in {standings.index(select)+1}o place')
