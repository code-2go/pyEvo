name = str(input('Enter a student complete name: ')).strip().title()
q1 = float(input('Enter a quarter 1: '))
q2 = float(input('Enter a quarter 2: '))
q3 = float(input('Enter a quarter 3: '))
q4 = float(input('Enter a quarter 4: '))
average = ((q1+q2+q3+q4)/4)
print(average)
if average < 5.0:
    print('The student, {} {}, is reproved!'.format(name.split()[0], name.split()[len(name.split())-1]))
elif (average >= 5.0) and (average <= 6.9):
    print('The student, {} {}, needs to go to summer school'.format(name.split()[0], name.split()[len(name.split())-1]))
else:
    print('The student, {} {}, passed! Congratulation.'.format(name.split()[0], name.split()[len(name.split())-1]))
