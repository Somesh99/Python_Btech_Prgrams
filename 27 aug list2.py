Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ##2d list or matrix
>>> x=[[1,2],[2,3,4,5],[10,20,30,40]]
>>> x[0]
[1, 2]
>>> len(x)
3
>>> len(x[1])
4
>>> del x[1]
>>> for i in range :
	print(i)

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    for i in range :
TypeError: 'type' object is not iterable
>>> for i in range:
	print(i)

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    for i in range:
TypeError: 'type' object is not iterable
>>> 
>>> 
>>>  for i in x:
	print(i)
	
SyntaxError: unexpected indent
>>> for i in x:
	print(i)

	
[1, 2]
[10, 20, 30, 40]
>>> x=[1,2,3,4]
>>> x=y
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    x=y
NameError: name 'y' is not defined
>>> x=y
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    x=y
NameError: name 'y' is not defined
>>> y=x
>>> id(x)
1098830215496
>>> id(y)
1098830215496
>>> y[1]=10
>>> y
[1, 10, 3, 4]
>>> x
[1, 10, 3, 4]
>>> x=[1,2,3,4]
>>> z=x[::]
>>> z
[1, 2, 3, 4]
>>> id(x)
1098830216776
>>> id(y)
1098830215496
>>> z[2]=200
>>> z
[1, 2, 200, 4]
>>> x
[1, 2, 3, 4]
>>> z[1]



