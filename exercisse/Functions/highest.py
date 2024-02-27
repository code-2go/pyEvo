# Create a program with fuction def highest(). This function receive unlimited integers paramerters 
# and return the highest value.


data = []


def highest():
    bigger = max(data)
    return bigger


while True:
    data.append(int(input('Enter an integer value: ')))
    check = str(input('Register another value? Yes or No\n').upper()[0])
    while check not in 'YN':
        check = str(input('Wrong awnser. Please, try again! Yes or No\n').upper()[0])
    if check == 'N':
        break
print(f'The highest value on the list is: {highest()}')
