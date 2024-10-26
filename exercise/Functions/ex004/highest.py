# Create a program with fuction def highest(). This function receive unlimited integers paramerters 
# and return the highest value.


def highest(*num):
    bigger = max(*num)
    print(f'The highest value on the list is: {bigger}')


highest(2, 4, 999, 10, 15, 30, 90, 33, 124)
highest(39, 29, 100, 99)
highest(59, 79, 150, 149, 5, 30, 90, 33, 12)

