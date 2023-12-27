# A professor need find one random student through a lottery.

import random

name1 = input('Enter a student name: ')
name2 = input('Enter a student name: ')
name3 = input('Enter a student name: ')
name4 = input('Enter a student name: ')
choice = random.choice([name1, name2, name3, name4])
pair = random.sample([name1,name2, name3, name4], k=2)
print ('The student chose is {} \nA pair of students is {}'.format(choice, pair))

#shuffle 

# name1 = input('Enter a student name: ')
# name2 = input('Enter a student name: ')
# name3 = input('Enter a student name: ')
# name4 = input('Enter a student name: ')
# name5 = input('Enter a student name: ')
# name6 = input('Enter a student name: ')
# name7 = input('Enter a student name: ')
# name8 = input('Enter a student name: ')
# deck = [name1, name2, name3, name4, name5, name6, name7, name8]
# random.shuffle(deck)
# print(deck)
