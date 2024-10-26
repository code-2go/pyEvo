words = ('apple', 'juice', 'amazing', 'gule', 'carton', 'binary', 'flavor', 'python')
for cnt in range(0, len(words)):
    broke = words[cnt].strip()
    print(f'\nThe {broke} word are the vowels -', end=' ')
    for letter in range(0, len(broke)):
        if broke[letter] in 'aeiou':
            print(f'{broke[letter]}', end=' ')
# method 2:
# for cnt in words:
#     print(f'\n{cnt}', end=' ')
#     for letter in cnt:
#         if letter in 'aeiou':
#             print(letter, end=' ')
