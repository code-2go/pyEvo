data = {}
bigdata = []
goals = []
sum = 0
while True:
    data['name'] = str(input('Enter the athlete name: ').title())
    data['matches'] = int(input('Enter the number of matches he has played: '))
    for cnt in range(0, data['matches']):
        while True:
            try:
                goals.append(int(input(f'Enter the number of goals he scored in the {cnt+1}o match: ')))
                break
            except ValueError:
                print('Invalid number')
                pass
    for cnt in goals:
         sum += cnt
    data['goals'] = goals[:]
    data['score'] = sum  
    sum = 0
    goals.clear()
    bigdata.append(data.copy())
    while True:
            try:
                check = int(input('Register another player?\n [1]YES or [2]NO - '))
                while check < 1 or check > 2: 
                    print('Invalid option. Try again!')
                    check = int(input('Register another player?\n [1]YES or [2]NO - '))
                break
            except ValueError:
                print('Invalid option! Please enter [1]YES or [2]NO. Try again!')
                pass
    if check == 2: 
        break
print()
print('Players registered:'.center(30))
print('-'*30)
print(f'{"No":<6}{"Name"}{"Score":>20}')
for cnt in range(0, len(bigdata)):
    print(f'{cnt+1:<6}{bigdata[cnt]['name']:.<20}{bigdata[cnt]['score']}')
while True:
    try:
        check = int(input('\nCheck deep data? [1]YES or [2]NO '))
        while check <1 or check > 2:
            print('Invalid option. Try again!')
            check = int(input('\nCheck deep data? [1]YES or [2]NO '))
            break
        if check == 1:
            detail = int(input('\nEnter the player (No) to data: '))
            for cnt in range(0, len(bigdata[detail-1]['goals'])):
                print(f' - In the {cnt+1}o  match, {bigdata[detail-1]['name']} scored {bigdata[detail-1]['goals'][cnt]} goals')
        if check == 2:
            print('\nThank You')
            break
    except ValueError:
        print('Invalid option! Try again!')
        pass