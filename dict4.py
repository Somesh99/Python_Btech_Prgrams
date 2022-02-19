x=[[0,0,0,0,1],[0,0,0,0,0],[0,2,0,0,0],[0,0,0,0,1],[3,0,0,0,0]]
for i in x:
    print(i)
## equivalent dictionary implementation
sp={(0,4):1,(2,1):2,(4,0):3}
print(sp)
for i in range(5):
    for j in range(5):
        print(sp.get((i,j),0),end=' ')
    print()          



for i in range(5):
    for j in range(5):
        print(sp.get((i,j),'*'),end=' ')
    print()



    
    
    
