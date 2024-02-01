n = []
for cnt in range(0, 5):
    n.append(int(input('Enter a number: ')))
# highest = max(n)
# lowest = min(n)
print(f'The highest number on the list is {max(n)} in postion:', end=' ')
for pos, cnt in enumerate(n):
    if cnt == max(n):
        print(f'{pos}', end=' ') 
print()
print(f'The lowest number on the list is {min(n)} in postion:', end=' ')
for pos, cnt in enumerate(n):
    if cnt == min(n):
        print(f'{pos}', end=' ')
