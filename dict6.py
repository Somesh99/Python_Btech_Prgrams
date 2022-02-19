## factorial using dictionary

fact={0:0,1:1}
for i in range(10):
    if i not in fact:
        fact[i]=i*fact[i-1]
print('factorial....5=',fact[5])
