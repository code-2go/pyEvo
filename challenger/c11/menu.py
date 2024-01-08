'''Create a program with read four values Menu, A, B, C and shows the under options: 
• if the menu = 1, Write A, B, C in ordered form; 
• if the menu = 2, Write A, B, C in descending order; 
• if the menu = 3, Write the values with the higher value in the middle position
• if the menu is different from the options offered, create an alert notice'''

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))
print('{0}\n1 - Write the values in ordered form. \n2 - Write the values in descending order. \n3 - Write the values with de higher value in the middle position.\n{0}'.format('='*70))
if a < b < c:
    smallest = a
    middle = b
    higher = c
elif a < c < b:
    smallest = a
    middle = c
    higher = b    
elif b < a < c:
    smallest = b
    middle = a
    higher = c
elif b < c < a:
    smallest = b
    middle = c
    higher = a
elif c < a < b:
    smallest = c
    middle = a
    higher = b
elif c < b < a:
    smallest = c
    middle = b
    higher = a
menu = int(input('Choose one: '))
if menu == 1:
    print(smallest, middle, higher)
if menu == 2:
    print(higher, middle, smallest)
if menu == 3:
    print(smallest, higher, middle)
if menu > 3:
    print('Wrong choice! Try again')
