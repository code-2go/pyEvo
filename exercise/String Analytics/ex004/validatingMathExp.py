#Code to validating a mathematical expression. Algorithm checks that its parentheses have their respective closing pair
exp = str(input('Write the mathematical expression for check: '))
checkPool = []
validExp = 0 #second validating to check for empty parantheses 
for pos, element in enumerate(exp):
    if element == '(' and exp[pos+1] == ')':
        print(f'Empty parantheses')
        validExp = 1
        break
    if element == '(':
        checkPool.append(element)
    if element == ')':
        if len(checkPool) > 0:
            checkPool.pop()
        else:
            checkPool.append(element)
            break
if len(checkPool) == 0 and validExp != 1:
    print('Valid expression')
else:
    print('Unvalid expression')
