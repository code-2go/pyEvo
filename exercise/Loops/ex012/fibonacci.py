f = int(input('How much steps should be displayed in the Fibonacci sequence? '))
f1 = 0
f2 = 1
cnt = 0
while cnt < (f):
    fn = f1 
    print(fn, end=' ')
    f1 = f2
    f2 = f1 + fn
    cnt += 1
