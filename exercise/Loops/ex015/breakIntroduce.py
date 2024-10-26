from random import randint
cnt = n = 0
while n != 999:
    n = randint(0, 999)
    print(n)
    if n == 999:
        break
    cnt += 1
print(f'It took {cnt} attempts to stop the process.')
