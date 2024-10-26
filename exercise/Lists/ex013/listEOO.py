'''Create an algorithm so that the user enters seven N values and then, if the value is even, 
it will be recorded in the respective even list, otherwise it will be recorded in the odd list.'''

data = [[], []]
for cnt in range(0,7):
    n = (int(input(f'Enter the pos {cnt} integer: ')))
    if n % 2 == 0:
        data[0].append(n)
    else:
        data[1].append(n)

print(f'The even numbers are: {sorted(data[0])}')    
print(f'The odd numbers are: {sorted(data[1])}')
