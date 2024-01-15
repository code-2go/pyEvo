from datetime import datetime
adult = 0
young = 0
today = datetime.today().year
for counter in range(0, 7):
    born = int(input('Enter the year you were born: '))
    if (today - born < 21):
        young += 1
        print('You are underage')
    else:
        adult += 1
        print('You are of legal age')
print('There are {} person of legal age and {} underage'.format(adult, young))
