form = []
data = []
patients = 0
highest = 0 
lowest = 0
while True:
    data.append(str(input('Enter the pacient name: ')).title())
    data.append(float(input('Enter the pacient Weight: ')))
    form.append(data[:])
    data.clear()
    check = str(input('Enter another pacient? Yes/No\n')).upper().strip()[0]
    patients += 1
    if check == 'N':
        break
for pos, cnt in enumerate(form):
    if pos == 0: 
        highest = lowest = form[pos][1]
    elif form[pos][1] < lowest:
        lowest = form[pos][1]
    elif form[pos][1] > highest:
        highest = form[pos][1]
for cnt in range(0, len(form)):
    if form[cnt][1] == highest:
        highest = form[cnt][0]
    if form[cnt][1] == lowest:
        lowest = form[cnt][0]
print(f'There are {patients} registered patients')
print(f'The patient with the lowest weight is {lowest} and patient with the highest weight is {highest}')
