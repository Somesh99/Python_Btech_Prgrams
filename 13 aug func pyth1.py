#factorial without recursion
def fact(n):
    y=1
    for i in range(1,n+1):
        y=y*i
    print('factorial of %d is %d'%(n,y))


x=int(input('enter a number'))
 
fact(x)


#factorial with recursion

def fact1(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)


x=int(input('enter a number'))
f=fact(x)
print('factorial of %d is %d'%(x,f))

#fibbonicci with recursion
#0 1 1 2 3 5 8 13 21 34 55

def fib(n):
    if n==0:
        return 0 
    elif n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
x=int(input('enter a number'))
f=fib(x)
print('fibonacci of %d is %d'%(x,f))
print('fibonacci series......')

for i in range(x+1):
    print(fib(i),end =' ')
    
    
# without recursion
def fib1(n):
    a,b,c=-1,1,0
    for i in range(n+1):
        c=a+b
        print(c)
        a=b
        b=c
x=int(input('enter a number'))
print('fibonacci series......')
fib1(x)


        



    
    



