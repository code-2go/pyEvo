#after n > 10000 the code will crash
# n = 10000
# for i in range(1, n):
#     divisor = 0
#     check = 0
#     for cnt in range(i, 0, -1):    
#         if i % cnt == 0:
#             check += cnt
#     if check-i == i :
#         print(i, end=' ')

#efective method: 
n  = 100
for i in range (1, n):
    divisor = 0
    for cnt in range(i, 0, -1):
        if i % cnt == 0:
            divisor += 1
    if divisor == 2:
        pf = (2**(i-1)*(2**i-1))
        print('{} is prime and your respective perfect number is {}'.format(i, pf))