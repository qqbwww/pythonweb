__author__ = 'qb.qian'


aStr = '123456789'

for i in [None] + range(-1,-len(aStr), -1):
    print aStr[:i]

bstr= 'abcdefghijkl'
print bstr[:None]