phrase = ("You cAn't teAch An old dog new tricks").lower().strip()
print('a' in phrase)
print('In this setence there are {} letters A, the first one is found on position {} and the last is in position {}.'.format(phrase.count('a'), phrase.find('a'), phrase.rfind('a')))
