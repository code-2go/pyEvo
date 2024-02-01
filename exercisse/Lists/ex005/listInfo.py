numbers = []
while True:
    numbers.append(int(input('Enter an integer: ')))
    check = str(input('Continue? Yes or No - ')).strip().lower()[0]
    if check == 'n':
        break
numbers.sort(reverse=True)
print(f'This list has {len(numbers)} numbers entered.')
print(f'(Decrease order of the list is {numbers})')
print('There are 5 on the list' if 5 in numbers else 'there is no 5 on the list!')