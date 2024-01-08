from math import ceil
object = float(input('How much does the house you want cost? '))
salary = float(input('Enter your wage: '))
deltaT = int(input('How long does it take to finalize the loan? \n[1] - 12 mounths \n[2] - 24 mounths \n[3] - 36 mounths\n[4] - other \n'))
if deltaT == 1:
    time = 12
elif deltaT == 2:
    time = 24
elif deltaT == 3:
    time = 36
elif deltaT == 4:
    time = int(input('Enter a number of mounths needed to finalize the loan: '))
payment = (object/time)
if payment < salary*1.3:
    print('Loan approved. Payment per mounth cost ${:.2f}'.format(payment))
else:
    print('Loan recused! You minimun loan period is {} mounths'.format(ceil(object/(salary*1.3))))