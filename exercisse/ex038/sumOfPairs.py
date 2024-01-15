from random import randint
sum = 0
for counter in range (0, 6):
    num = randint(0, 100)
    print('number {}: {}'.format((counter+1), num))
    if num%2 == 0:
        sum += num
print(sum)