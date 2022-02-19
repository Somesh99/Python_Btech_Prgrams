x=input('enter words with spaces')
import string
a=x.find(' ')
print(a)
print('first word=',x[0:a])
b=x.rfind(' ')
print(b)
print('last word=',x[b+1:])


