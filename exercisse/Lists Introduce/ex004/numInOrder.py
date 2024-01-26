numbers = []
for cnt in range(0, 5):
    print(f'tamanho da lista {len(numbers)}\n')
    n = int(input('Enter an number: '))
    if len(numbers) == 0 or n > numbers[-1]:
        numbers.append(n)
    else:
        for pos, cnt in enumerate(numbers):
            if n <= cnt:
                 numbers.insert(pos, n)
                 break
print(numbers)
