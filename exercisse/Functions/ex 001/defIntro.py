# Create a program with def area() to receive the plot sizes, width and heigh of the retangle plot. At the end,
# display the floor area.


def area():
    width = int(input('Enter the wide: '))
    height = int(input('Enter the height: '))
    m_area = width * height
    print(f'The floor area is {m_area} m²')


def frame():
    print('.' * 30)


frame()
print('Enter the plot sizes:'.center(30))
frame()
area()
