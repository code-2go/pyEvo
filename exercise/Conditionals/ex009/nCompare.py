from random import randint
n1 = int(randint(0,10))
n2 = int(randint(0,10))
print(n1, n2)
if n1 > n2:
    print('{} is higher than {}.'.format(n1, n2))
elif n1 < n2:
    print('{} is higher than {}.'.format(n2, n1))
else:
    print('Both have the same value')
