# matrix = [[], [], []]
# for cnt in range(0, 9):
#     n = (int(input('Enter an integer: ')))
#     if cnt < 3:
#         matrix[0].append(n)
#     elif cnt >= 3 and cnt < 6:
#         matrix[1].append(n)
#     else:
#         matrix[2].append(n)
# for x in range(0, 3):
#     for y in range(0, 3):
#         print(f'{matrix[x][y]:^5}', end='')
#     print()

from random import randint
matrix = []
data = []
evenSum = colum_3 = highest = 0

for cnt in range(0, 9):
    data.append(randint(0, 40))
    if len(data) >= 3:
        matrix.append(data[:])
        data.clear()
for x in range(0, 3):
    for y in range(0, 3):
        if matrix[x][y] % 2 == 0:
            evenSum += matrix[x][y]
        if y == 2:
            colum_3 += matrix[x][y]
        if x == 1 and y == 0:
            highest = matrix[x][y]
        elif x == 1:
            if matrix[x][y] > highest:
                highest = matrix[x][y]
        print(f'{matrix[x][y]:^8}', end='')
    print()
print(f'In the matrix, the sum of the all the evens is: {evenSum}')
print(f'The sum of the third colum is: {colum_3}')
print(f'The highest value in the second line is: {highest}')