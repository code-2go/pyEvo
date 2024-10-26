from random import randint
velocity = randint(0,200)
print(velocity)
trafficFine = (velocity-80)*7
if velocity > 80:
    print('You have exceeded the traffic limit. Your traffic ticket cost ${}'.format(trafficFine))
else:
    print('Congratulations on your safe driving')