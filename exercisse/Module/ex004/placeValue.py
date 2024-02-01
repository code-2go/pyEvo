from random import randint
import math

#str form
# n = randint(0,9999)
# convert = str(n)
# print('ones: {0}\ntens: {1}\nhundreds: {2}\nThousands: {3}'.format(convert[3],convert[2], convert[1], convert[0]))

#math form
n = randint(0,9999)
print(n)
    #exemple method:
    #n=1234
    #n//1 == 1234 :. 1234%10 == 123.4 remainder 4 (ones)
    #n//10 == 123 :. 123%10 == 12.3 remainder 3 (tens)
    #n//100 == 12 :. 12%10 == 1.2 remainder 2 (hundreds)
    #n//1000 == 1 :. 1%10 == 0.1 remainder 1 (thousands)
print('Ones: {}\nTens: {}\nHundreds: {}\nThousands: {}'.format((n//1)%10, (n//10)%10, (n//100)%10, (n//1000)%10))
