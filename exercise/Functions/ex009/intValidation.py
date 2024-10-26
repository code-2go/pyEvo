# Create a function that takes as input a value and outputs an integer validation. It's functon only accepts integers.
# Another method for int(input( )).


def checkInt(msg):
    """
    This function check if the entered value is an integer number. If any other type is entered, the code not be
    interrupted and the process will be repeated until an integer number is entered.
    :param msg: the value that was entered
    :return: the integer value
    """
    check = False
    value = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            value = int(n)
            check = True
        else:
            print('WRONG! Enter a integer')
        if check:
            break
    return value
            

num = checkInt('Enter a integer number: ')
print(f'{num} is a integer number')
