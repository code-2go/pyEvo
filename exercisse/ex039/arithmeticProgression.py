# start = int(input('Enter the number to start the progression: '))
# ratio = int(input('Choose the arithmetic ratio: '))
# #aProgression = start+(10-1)*ratio
# for counter in range(start, ((start+(10-1)*ratio) + ratio), ratio):
#      print(counter)


#Other method
start = int(input('Enter a first number to progression '))
ratio = int(input('Enter the arithmetic ratio: '))
opt = 1
while opt != 2:
     start += ratio
     print(start)
     opt = int(input('Do you want to show the next number in the progression? [1] YES - [2] NO'))
