''' Create a program for read a name and two grades of n students and record them in a composite list. At the end display the student card with the average of each students and show the user the posibility of seeing the grades of an individual students. '''

student = []
data = []
average = []
while True:
    data.append(str(input('Enter student name: ')).title())
    data.append(float(input('Enter student Q1: ')))
    data.append(float(input('Enter student Q2: ')))
    student.append(data[:])
    average.append((student[len(student)-1][1]+student[len(student)-1][2])/2)
    data.clear()
    checkTrue = str(input('Enter another student? Yes/No ')).strip().lower()[0]
    while checkTrue not in 'yn':
        checkTrue = str(input('Wrong answer. Please try again.\nEnter another student? Yes/No ')).strip().lower()[0]
    if checkTrue == 'n':
        break
print('-'*20)
print(f'Number - Student  -  Average')
for cnt in range(0, len(student)):
    print(f'{cnt+1:<6} - {student[cnt][0]:<15} {average[cnt]}')
print(student)
individualGrade = int(input('If you wish, enter a student number to check their individual grade. Press 0 to cancel. - '))
while individualGrade > len(student):
    individualGrade = int(input('Wrong answer! Please try again.\nEnter a student number to check their individual grade. Press 0 to cancel. - '))
if individualGrade != 0:
    print(f'{student[individualGrade-1]}')
elif individualGrade == 0:
    print('Thank You!')
