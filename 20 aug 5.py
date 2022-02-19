x=input('enter email id')
 
at= x.find('@')
dot= x.rfind('.')
ac=x.count('@')
if at>1 and ac==1 and dot>at+3 and dot+2<=len(x):
    print('valid')
else:
    print('invalid')

