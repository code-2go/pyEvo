'''Create an algorithm that shows a math table from 1 to 10 with some info for 1 to 10 such as: the number, the power of 2, the power of 3, the factorial, the number of divisors and wheter the number is prime'''

print('number   -   power2   -   power3   -   factorial   -   divisors   -   prime')
n = 1
for cnt in range(1, 11):
    div = 0
    n = cnt*n
    for cnt2 in range(10, 0, -1): 
        if cnt % cnt2 == 0:
            div += 1
        if div == 2:
            prime = 'Yes'
        else:
            prime = 'No'
    print('{0}{1}{2}{3}{4}{5}'.format(str(cnt).center(6), str(cnt**2).center(20), str(cnt**3).center(6), str(n).center(22), str(div).center(7), str(prime).center(21)))