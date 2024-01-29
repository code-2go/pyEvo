from random import randint
list100 = []
for cnt in range(0, 20):
    list100.append(randint(0,10))
print(list100)
if 0 in list100:
    for pos, cnt in enumerate(list100):
        if cnt == 0:
            list100.pop(pos)
            list100.insert(pos, 1)
print('No nulls on the list:')
print(list100)