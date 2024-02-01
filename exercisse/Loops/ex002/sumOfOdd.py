# sum = 0
# for count in range(0,500+1):
#     if (count % 2 == 1) and (count % 3 == 0):
#         sum = sum + count
# print(sum)

#economic process method

sum = 0
for count in range(1, 500+1, 2):
    if count % 3 == 0:
        sum += count
print(sum, end=' ')
