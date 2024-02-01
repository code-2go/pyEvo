lower = 0
greater = 0
for counter in range(0,5):
    weight = float(input('Enter your weight: '))
    lower = weight
    if weight < lower:
        lower = weight
    elif weight > greater:
        greater = weight
print('The greater weight is {} and the lower weight is {}'.format(greater, lower))