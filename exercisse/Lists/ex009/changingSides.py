# Moving the first five to the last five
dataN = [1, 2, 3, 4, 5,
         6, 7, 8, 9, 10,
         11, 12, 13, 14, 15, 
         16, 17, 18, 19, 20]
for cnt in range(0, 5):
    aux = (dataN[cnt])
    dataN.pop(cnt)
    dataN.insert(cnt, cnt+16)
    dataN.pop(cnt+15)
    dataN.insert(cnt+15, aux)
print(dataN)