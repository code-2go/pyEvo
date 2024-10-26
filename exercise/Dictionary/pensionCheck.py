from datetime import date
citizen = {}
citizen['name'] = str(input('Enter the name: ')).title().strip()
year = int(input('Enter the birth year: '))
citizen['age'] = date.today().year - year
citizen['work card'] = int(input('Enter the work card. If you are minor or don\'t have a job, press 0(zero):  '))
if citizen['work card'] != 0:
    citizen['contribution time'] = int(input('Enter the numbers of years you have worked: '))
    citizen['retirement'] = 35 - citizen['contribution time']
    citizen['income'] = float(input('Please enter your salary: '))
    print(f'The Mr(a). {citizen["name"]}, {citizen["age"]} years old. His work permit number is: {citizen["work card"]} and he will be retire in {citizen["retirement"]} years. His last income is ${citizen["income"]}.')
else:
    if citizen['age'] < 18:
        print(f'The Mr(a). {citizen["name"]}, {citizen["age"]} years old. He\'s not old enough to work.')
    else:
        print(f'The Mr(a). {citizen["name"]}, {citizen["age"]} years old. He\'s never had a job.')