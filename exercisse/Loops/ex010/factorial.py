from math import factorial

# num = int(input('Enter an integer: '))
# n = 1
# for cnt in range(1, num+1):
#     n = n * cnt
# print(n)

# other method
num = int(input('Enter an integer: '))
n = num
for cnt in range(num, 2, -1):
    print('{} x {} = {}'.format(n, cnt-1, n*(cnt-1), end='\n'))
    n = n*(cnt-1)
print('')
print('{}! is {}'.format(num, n))

# math lib method

# num = int(input('Enter an integer: '))
# n = factorial(num)
# print(n)