## fibANOCCI series using dictionary
N=int(input("enter number of fbb series"))
x={}
fib={0:0,1:1}
for i in range(N):
    if i not in fib:
        fib[i]=fib[i-1]+fib[i-2]
print('fibonnaci series....')
print(fib.values())
print(fib)
        
 
    
