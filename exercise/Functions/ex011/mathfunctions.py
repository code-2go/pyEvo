def factor(n):
    f = 1
    for counter in range(n, 0, -1):
        f *= counter
    return f


def increase(value=0, tax=0):
    price = value * ((tax / 100) + 1)
    return price


def decrease(value=0, tax=0):
    price = value - (value * (tax / 100))
    return price


def double(value=0):
    multi = (value * 2)
    return multi


def half(value=0):
    div = value / 2
    return div


def coin(value=0, type='R$'):
    return f'{type} {value:.2f}'.replace('.', ',')


def note(value = 0, i = 0, d = 0):
    print('='*41)
    print('Values Note'.center(41))
    print('='*41)
    print(f'Twice {coin(value)} is \t\t{coin(double(value))}')
    print(f'Half of {coin(value)} is \t\t{coin(half(value))}')
    print(f'The {i}% increase of {value} is \t{coin(increase(value, i))}')
    print(f'The {d}% discount of {value} is \t{coin(decrease(value, d))}')