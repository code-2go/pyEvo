#Arithmetric method
import string
binary = []
octal = []
hexa = []
print('=-'*25)
number = int(input('Enter a number and choose a converter base: '))
print('=-'*25)
converter = int(input('[1] - Decimal to Binary \n[2] - Decimal to Octal \n[3] - Decimal to Hexadecimal \n'))
# #code for decimal to binary converter
if converter == 1:
    quocient = number
    if quocient == 0:
        binary.append(0)
    else:
        while quocient//2 != 0:
            remainder = quocient%2
            quocient = quocient//2
            binary.append(remainder)
            if quocient//2 == 0:
                binary.append(1)
    binary.reverse()
    print(f'The number {number} in its binary form is: ', end=' ')
    for cnt in binary:
        print(cnt, end='') 
# #code for decimal to octal converter 
if converter == 2:
    quocient = number
    if quocient >= 8:
        while quocient >= 8:
            remainder = quocient % 8
            quocient = quocient//8
            octal.append(remainder)
        if quocient < 8:
            octal.append(quocient)
    octal.reverse()
    print(f'The number {number} in its octal form is: ', end=' ')
    for cnt in octal:
        print(cnt, end='')
#code for decimal to hexadecimal converter 
if converter == 3:  
    quocient = number
    if quocient == 0:
         hexa.append(0)
    else:
        while quocient > 0:
            if quocient < 10:
                hexa.append(quocient)
                break
            remainder = quocient % 16
            quocient = quocient//16
            if remainder < 10:
                hexa.append(remainder)   
            if remainder >= 10 and remainder <= 15:
                for cnt in range(0, 6):
                    if remainder == cnt + 10:
                        hexa.append(string.ascii_uppercase[cnt])     
    hexa.reverse()
    print(f'The number {number} in its hexadecimal form is: ', end=' ')
    for cnt in hexa:
            print(cnt, end='')