# Create a program with the counter function that receives three parameters: start, end and pass; 
# and then returns a count type for option C.
# A) count up from 0 to 10, pass 1
# B) count down from 10 to 0, pass 2
# C) Custom the count (start; end; pass)
from time import sleep


def count_up():
    sleep(1)
    for counter in range(1, 10 + 1):
        print(counter, end=' ')
        sleep(.1)
    print('End.')


def count_down():
    sleep(1)
    for counter in range(10, 0, -1):
        print(counter, end=' ')
        sleep(.1)
    print('End.')


def custom():
    sleep(1)
    start = int(input('Enter an integer to start your count: '))
    end = int(input('Enter an integer to stop your count: '))
    counting_pass = int(input('Enter an integer number, positive or negative, for the pass counter: '))
    for counter in range(start, end + counting_pass, counting_pass):
        print(counter, end=' ')
        sleep(.1)
    print('End.')


count_up()
count_down()
custom()
