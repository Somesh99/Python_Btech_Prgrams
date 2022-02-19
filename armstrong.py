x=input("enter a number")
y=len(x)
temp=0
for i in x:
      temp+=int(i)**10
if x==str(temp):
   print('armstrong')
else:
   print('no')
   
