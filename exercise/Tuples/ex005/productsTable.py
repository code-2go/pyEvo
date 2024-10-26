products = ('pencils', 3.25, 'paper pack', 10, 'gule', 1.5, 'paper folders', 1.2, 'coffe paper', 0.8, 'scissors', 3, 'plastic cups', 3.5, 'erasers', 1.2, 'pen', 1.2, 'mechanical pen', 8)

print(('Office shopping list').center(35))
print('='*40)
for item in range(0, len(products)):
    if item % 2 == 0:
        print(f'{products[item]:.<34}', end='')
    else:
        print(f'${products[item]:>5.2f}')