from random import randint
numbers = (randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20))
print(numbers)
lower = greater = 0
for cnt in range(0,5):
    if lower == greater == 0: 
        lower = greater = ((numbers)[cnt])
    elif lower > ((numbers)[cnt]):
        lower = ((numbers)[cnt])      
    elif greater < ((numbers)[cnt]):
        greater = ((numbers)[cnt])      
print(f'Lower tuple number : {lower}\nGreater tuple number: {greater}')
