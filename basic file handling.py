##wap to create a file with some content
#f=open('abd.txt','w')
#f.write('this is my python class.\ni like python programming.')
#f.close()


##wap to read a file and display its contains
#f=open('abd.txt','r')
#print(f.read())
#f.seek(0)
#print(f.read())
#print(f.readline())
#print(f.readlines())
#print('number of char',len(f.read()))
#f.seek()
#print('number of lines',len(f.readlines()))

##wap to copy the content of one file to another file
#f1=open('abd.txt','r')
#f2=open('abc1.txt','w')
#f2.write(f1.read())
#f1.close()
#f2.close()

##waf that asked two arguments newfile and oldfile name,copy the content of oldfile to anewfile only those line that start with #

#f1=open('abd.txt','r')
#f2=open('abc1.txt','w')
##while True:
   # t=f1.readline()
   # if t=='':
      #  break
    #if t[0]=='#':
       # f2.write(t)
   ## else:
        #continue
#f1.close()
#f2.close()

##wap to read a file and count no of characters,lines in a file

##wap to write a variable inside a file
#f=open('abd2.txt','w')
#x=10
#y=23.56
#f.write('%d\n'%x)
#f.write('%f\n'%y)
#f.write('%.6f'%y)

#'%d'%23
#'%5d'%23
#'%-5d'%23
#'%f'%23.456
#'%.2f'%23.456
#'%10.2f'%23.456
#'%-10.2f'%23.456

### wap to write the contents of a variables with a proper datatype
import pickle
f=open('abc.pck','wb')
x=10
y=20.345
z=[12,'w23',230342354]
pickle.dump(x,f)
pickle.dump(y,f)
pickle.dump(z,f)
f.close()
##
f=open('abc.pck','rb')
x=pickle.load(f)
print(x)
print(type(x))
x=pickle.load(f)
print(x)
print(type(x))
x=pickle.load(f)
print(x)
print(type(x))
'%2.2f'%23.456


f.close()


