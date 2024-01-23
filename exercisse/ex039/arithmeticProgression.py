# start = int(input('Enter the number to start the progression: '))
# ratio = int(input('Choose the arithmetic ratio: '))
# #aProgression = start+(10-1)*ratio
# for counter in range(start, ((start+(10-1)*ratio) + ratio), ratio):
#      print(counter)


#Other method
# start = int(input('Enter a first number to progression '))
# ratio = int(input('Enter the arithmetic ratio: '))
# opt = 1
# while opt != 2:
#      start += ratio
#      print(start)
#      opt = int(input('Do you want to show the next number in the progression? [1] YES - [2] NO'))


#another way
open = int(input('Start number: '))
ratio = int(input('PA ratio: '))
n = int(input('Displayed numbers: '))
start = open
cnt = 0
totaly = 0
while cnt < n:
     print(start, end=' ')
     start += ratio
     cnt += 1
     totaly += 1
plus = 1
while plus != 2:  
     plus = int(input('\nShown more numbers? \n[1] YES [2] NO\n'))
     if plus != 1 and plus != 2:
          plus = int(input('Wrong choice!\nShown more numbers? \n[1] YES [2] NO\n'))
     cnt = 0
     if plus == 1:
          n = int(input('How many numbers should be displayed? '))
          while cnt < n:
               print(start, end=' ')
               start += ratio
               cnt += 1
               totaly += 1
     else:
          print('\nYou have vizualized {} arithmetic progressions to {} in the ratio {}'.format(totaly, open, ratio))
