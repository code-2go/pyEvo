bigData = []
data = {}


def header():
    msg = 'Student\'s Grading System'
    print(msg)
    print('-'*len(msg))


def condition():
    opt = int(input('For check the class situation pick [1] for YES or [2] for NO\n'))
    if opt == 1:
        return True
    else:
        return False


def studentGrade(opt=False):
    sum = total = 0
    bigData.append(float(input('Enter the student score: ')))
    bigData.sort()
    data['max'] = round(bigData[-1], 1)
    data['min'] = round(bigData[0], 1)
    for cnt in range(0, len(bigData)):
        total += 1
        sum += bigData[cnt]
        avg = sum / len(bigData)
    data['avg'] = round(avg, 1)
    data['total'] = total
    if opt:
        if avg >= 8:
            data['situation'] = 'Good'
        elif 6 < avg < 8:
            data['situation'] = 'Medium'
        else:
            data['situation'] = 'Bad'
    return data


header()
option = condition()
print(studentGrade(opt=option))
while True:
    check = int(input('Recorder student score? [1] YES or [2] NO\n'))
    if check == 1:
        print(studentGrade(opt=option))
    else:
        break
