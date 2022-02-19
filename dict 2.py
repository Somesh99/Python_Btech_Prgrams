x={0:0,1:1,2:8,3:27,4:64,5:125,6:216,7:243,8:512,9:729,10:1000}
for i in x:
    print(i, 'cube is' ,x[i])
print(len(x))
print(type(x))
print(x.keys())
print(x.items())
print(x.values())
    
## insertion
x[11]=121*11
print(x)
## delete
del x[11]
print(x)

## another method
cube={x:x**5 for x in range (11)}
for k in x:
    print(k,'-',x[k])
## 2nd programe
x={i:i**3 for i in range(11)}
print(x)

for k,v in x.items():
    print(k,'-',v)
