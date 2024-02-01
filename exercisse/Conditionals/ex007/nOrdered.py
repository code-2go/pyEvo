from random import randint
n1 = randint(0,10)
n2 = randint(0,10)
n3 = randint(0,10)
print(n1,n2,n3)
if n1 < n2 < n3:
    smallest = n1
    higher = n3
if n1 < n3 < n2:
    smallest = n1
    higher = n2
if n2 < n1 < n3: 
    smallest = n2 
    higher = n3
if n2 < n3 < n1:
    smallest = n2
    high = n1
if n3 < n1 < n2:
    smallest = n3
    higher = n1
if n3 < n2 < n1: 
    small = n3
    higher = n1

print('Smallest: {} \nHigher: {}'.format(smallest, higher))