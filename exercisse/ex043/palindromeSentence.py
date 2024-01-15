sentence = str('Step on no pets').strip().lower().split()
gule = ''.join(sentence)
reverse = (gule[::-1])
print(gule)
print(reverse)
if gule == reverse:
    print('This sentence is a palindrome')
else:
    print('This sentence isn\'t a palindrome')