# n = int(input('Enter an integer: '))
# for c in range(1, n+1):
#     if c%2==0:
#         print(c, end=' ')

#economic method 

n = int(input('Enter an integer: '))
for c in range(2, n+1, 2):
    print(c, end=' ')
