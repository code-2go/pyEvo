from random import randint
l1 = randint(1,10)
l2 = randint(1,10)
l3 = randint(1,10)
print('l1: {}\nl2: {}\nl3: {}'.format(l1, l2, l3))
if (l1+l2 > l3) and (l1+l3 > l2) and (l2+l3 > l1):
    if(l1 == l2) and (l2 == l3):
        print('The triangle is equilateral')
    elif (l1 == l2) and (l2 != l3) or (l1 == l3) and (l3 != l2) or (l2 == l3) and (l3 != l1):
        print('The triangle is isoceles')
    elif (l1 != l2) and (l2 != l3):
        print('The triangle is scalene')
else:
    print("There are no condition to create a triangle")
