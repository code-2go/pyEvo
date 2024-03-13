# Create a factorial function. It receives two parameters: the first is the number to be factored 
# and the second is the boolean condition for displaying the factorial process of the entered number


def factor(num, check=False):
    f = 1
    for cnt in range(1, num+1):
        if check == True:
            print (f'{f} x {cnt} = {f*cnt}')
        f *= cnt      
    return f
    

n = int(input('Enter an integer to factor: '))
print(f'The {n} factor is {factor(n, True)}')
