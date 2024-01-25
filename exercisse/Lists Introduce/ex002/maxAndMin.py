n = []
for cnt in range(0, 5):
    n.append(int(input('Enter a number: ')))
highest = max(n)
lowest = min(n)
for pos, cnt in enumerate(n):
    if cnt == highest:
        print(f'The highest number on the list is {highest} in postion {pos}')
    if cnt == lowest:
        print(f'The lowest number on the list is {lowest} in postion {pos}')