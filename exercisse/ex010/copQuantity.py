width = float(input('Enter the wall width (in centimeter): '))
height = float(input('Enter the wall height (in centimeter): '))
wConversor = width/100
hConversor = height/100
# 1 = wconversor = 2 + hConversor = 2
print('For a {}m x {}m wall, you need {} can of paint to paint all of the wall.'.format(wConversor, hConversor, width/height))
