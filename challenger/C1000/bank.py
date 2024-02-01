banknote50 = banknote20 = banknote10 = banknote01 = 0
withdraw = (input('How much money to withdraw: $ '))
if withdraw.isnumeric() == False:
    while withdraw.isnumeric() != True:
        withdraw = (input('Enter a valid value! \nHow much money to withdraw: $ '))
converter = (int(withdraw))
while converter > 0:
    if converter >= 50:
        banknote50 += 1
        converter -=  50
    elif converter >= 20:
        banknote20 += 1
        converter -= 20
    elif converter >= 10:
        banknote10 += 1
        converter -=  10
    elif converter >= 1:
        banknote01 += 1
        converter -= 1
print('-- You obtained:')
if banknote50 > 0:
    print(f'{banknote50}, 50 dollar bill')
if banknote20 > 0:
    print(f'{banknote20}, 20 dollar bill')
if banknote10 > 0:
    print(f'{banknote10}, 10 dollar bill')
if banknote01 > 0:
    print(f'{banknote01}, 01 dollar bill')