# Algorithm that writes twenty random numbers sorted in a list and then writes  ten more numbers inserted in the sorted position
from random import randint
nList = []
# code to writes the first twenty
for cnt in range (0,20):
    nList.append(randint(0, 20))
# sorted list
nList.sort()
print(nList)
# algorithm that inserts the last ten numbers and displays
for cnt in range(0, 10):
    n = (randint(0,20))
    print(n, end='..')
    # guidance fpr sorting the number entered in the list
    for pos, cnt2 in enumerate(nList):
        if n <= cnt2:
            nList.insert(pos, n)
            # Once the list has been sorted, stop the looping
            break
print(f'\n{nList}')