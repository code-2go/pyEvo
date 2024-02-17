data = {}
goals = []
sum = 0
data['name'] = str(input('Enter the athlete name: '))
data['matches'] = int(input('Enter the number of matches he has played: '))
for cnt in range(0, data['matches']):
    goals.append(int(input(f'Enter the number of goals he scored in the {cnt+1}o match: ')))
    sum += goals[cnt]
    data['score'] = sum
print()
print(f'The {data["name"]}\'s statistics:'.center(46))
print('-'*46)
#for keys, values in data.items():
print(f'The number of matches: {data["matches"]}')
print(f'The total goals in the current championship: {data["score"]}')
for cnt, goals in enumerate(goals):
    print(f' - In the {cnt+1}o match, {data["name"]} scored {goals} goals')