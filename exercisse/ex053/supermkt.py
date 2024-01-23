sum = qnt = cheap = expensive = hundredPrice = 0
while True:
    product = str(input('Enter the product name: ')).strip().title()
    if product.isalpha() == False:
        while product.isalpha() != True:
            product = str(input('I don\'t understand. Please, enter the product name again: ')).strip().title()
    price = float(input('Enter the price: $ '))
    print(f'The {product} costs ${price}')
    sum += price
    qnt += 1
    if cheap == expensive == 0:
        cheap = expensive = price
        cheapName = expensiveName = product
    elif cheap > price:
        cheap = price 
        cheapName = product
    elif expensive < price:
        expensive = price
        expensiveName = product
    if price > 100: 
        hundredPrice += 1
    check = int(input('Enter another product?\n[1] Yes - [2] No\n'))
    if check == 2:
        break
print(f'''• The purchase had {qnt} items and the total was $ {sum}. 
• Purchases had {hundredPrice} items thats cost more than $ 100.00.
• The cheapest product is {cheapName} which cost $ {cheap} and the most expensive is {expensiveName} which costs $ {expensive}''')