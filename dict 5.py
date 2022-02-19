### wap to count occurence of each alpkabet in a giveen tring
    
y='lovely professional university'
cc={}
for i in y:
    cc[i]=cc.get(i,0)+1
print(cc)
for i in cc:
    print(i,'-',cc[i])
print(cc.keys())



