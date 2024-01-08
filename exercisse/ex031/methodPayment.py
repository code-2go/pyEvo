cost = float(input('Enter the purchase cost: $'))
debit = cost*0.9
credit = cost*0.95
installment2 = cost
installment3 = cost*1.2
print('[1] Debit \n[2] Credit\n[3] Installment 2x\n[4] Installment 3x or more')
method = int(input('Chose a mode of payment: '))
if method == 1:
    print('The final cost is $', debit)
elif method == 2:
    print('The final cost is $', credit)
elif method == 3:
    print('The final cost is 2x $',(installment2/2))
elif method == 4:
    times = int(input('How many times do you need to pay in installments? '))
    print('The final cost is {}x ${}'.format(times, installment3/times))
