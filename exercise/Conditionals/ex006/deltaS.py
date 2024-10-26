distance = float(input('In kilometers, how far is your trip? '))
if distance <= 200:
    value = distance*0.5
else:
    value = distance*0.45
print('Your ticket costs ${:.2f}'.format(value))