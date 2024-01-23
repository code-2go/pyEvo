while True:
    mult = int(input('Enter a factor to create a multiplication table of your product: '))
    for cnt in range(0, 10+1):
        print(f'{mult} x {cnt} = {mult*cnt}')
    check = str(input('Do you need another table? Answer YES to continue or NO to stop program.\n')).strip().lower()[0]
    if check in 'Nn':
        confirm = int(input('Please confirme you exit. \n[1] Confirme [2] Back to start\n'))
        if confirm == 1:
            break
    while check not in 'yn': 
        check = str(input('I don\'t understand. Please, answer YES to continue or NO to stop program.\n')).strip().lower()[0]
print('Thank You!')