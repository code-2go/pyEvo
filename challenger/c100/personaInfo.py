from math import floor
option = 1
youngGirl = 0
older = 0
cnt = 1
sum = 0
average = 0
while option != 2:
    name = str(input('Name: ')).strip()
    age = int(input('Age: '))
    gender = str(input('Gender: ')).strip().lower()
    if gender == str('male'):
        if age > older:
            older = age   
            print('The oldest man is {} with {} years old'.format(name, age)) 
    if gender == str('female'):
        if age < 20:
            youngGirl += 1 
    #Average:               
    sum += age
    average = sum/cnt
    option = int(input('Do you wanna register a person in group? \n[1] - YES \n[2] - NO \n'))
    if option == 1:
        cnt += 1
    else:
        print('The year group average is {} years old.'.format(floor(average)))
        print('This group has {} girls under 20'.format(youngGirl))
