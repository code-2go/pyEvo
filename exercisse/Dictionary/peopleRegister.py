'''Create a program to read a name, gender and age of an indefinite number of people. 
Record the data in a specific dictionary, for ex.: dic["names:"], dic["genders: "]. 
And all these dictionaries in a list. At the end, display:

a - how much people are registered
b - average of all registered ages
c - a list of all womans
d - a list of all people over the average age'''

data = {}
bigdata = []
sumAge = 0
while True:
    data['name'] = str(input('Enter the name: ').title().strip())
    data['gender'] = str(input('Enter the gender F/M: ').upper().strip()[0])
    while data['gender'] not in 'FM':
        data['gender'] = str(input('Wrong awnser. Enter the gender F/M: ').upper().strip()[0])    
    while True:
        try:
            data['age'] = int(input('Enter the age: '))
            break
        except ValueError:
            print('Please, enter a integer number to age. Try again!')
            pass
    bigdata.append(data.copy()) 
    while True:
        try:
            check = int(input('Register another person?\n [1]YES or [2]NO - '))
            while check < 1 or check > 2: 
                print('Invalid option! Please enter [1]YES or [2]NO. Try again!')
                check = int(input('Register another person?\n [1]YES or [2]NO - '))
            break
        except ValueError:
            print('Invalid option! Please enter [1]YES or [2]NO. Try again!')
            pass
    if check == 2: 
        break
for cnt in range(0, len(bigdata)):
    sumAge += bigdata[cnt]['age']
    average = sumAge/len(bigdata)
print()
print('Data info:'.center(55))
print('-'*55)
print(f'There are {len(bigdata)} people registered') 
print(f'\nThe average age of all the people registered is {average:.2f} years.')        
print('\nThe list of all registered women:')
for data in bigdata:
    if data['gender'] == 'F':
        print(f' Name: {data['name']}, age: {data['age']}')
print('\nThe list of all over the average age people:')
for data in bigdata:
    if data['age'] > average:
        for key, value in data.items():
            print(f' {key}: {value}', end=';')
        print()