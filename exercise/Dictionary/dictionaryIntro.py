'''Make a program to read a student name and their average and storage the student situation (reproved, aproved) in the dictionary. At the end, diplay the student card struture'''

data = {}
data['name'] = str(input('Enter a student name: '))
data['average'] = float(input('Enter the student average: '))
if data['average'] >= 7:
    data['situation'] = 'Aproved'
else:
    data['situatuin'] = 'Reproved'
print('No   student   average   situation')
print(f'{1:<5}{data["name"]:>5}{data["average"]:>8}{data["situation"]:>14}')