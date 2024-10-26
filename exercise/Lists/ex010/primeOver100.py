primeList = []
p10 = 0
for cnt in range(100, 200): 
    if (cnt % 2 == 0) and (p10 < 10):
        p10 += 1
        primeList.append(cnt)
print(primeList)
    