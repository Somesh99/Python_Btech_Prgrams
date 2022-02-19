#wap to access atributes


class time:
   'this is time class,havingattributes a,b,c'
   def __init__(tab,h,m,s):
        tab.a=h
        tab.b=m
        tab.c=s



   def showtime(tab):                                    
       # print(tab.a,':',tab.b,':',tab.c)
        print('time <'+str(tab.a)+':'+str(tab.b)+':'+str(tab.c)+'>')



t1=time(1,40,30) 
t2=time(5,55,50)
t1.showtime()
print(hasattr(t1,'a'))
print(hasattr(t1,'hour'))
print(getattr(t1,'a'))
setattr(t1,'a',20)
t1.showtime()
print(getattr(t1,'a'))
delattr(t1,'a')
print(hasattr(t1,'a'))
t1.showtime()

        
