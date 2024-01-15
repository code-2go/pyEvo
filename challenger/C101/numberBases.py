#Arithmetric method

number = int(input('Enter a number and choose a converter base: '))
#converter = int(input('[1] - Decimal to Binary \n[2] - Decimal to Octal \n[3] - Decimal to Hexadecimal \n'))
quocient = number
if quocient == 0:
    print(0)
else:
    while quocient//2 != 0:
        remainder = quocient%2
        quocient = quocient//2
        print(remainder, end='')
        if quocient//2 == 0:
            print(1)

# ajust reverse print. How? I don't know :(
# alternative  1 : I need to put data in list and then print this reverse list