## WAP to use the destructor...

class employee:
    def __init__(self):  ### constructor
        self.name='somesh' ### public
        self.__age=19     ###  private
    def disp(self):
        print(self.name,self.__age)
    def __del__(self):     ### desctructor
        classname=self.__class__.__name__  ### to know class name
        print("object of",classname,"has been destroyed")
e1=employee()     ### object creation
e1.disp()### calling member function

e2=e1 ### copy constructor
del e1
del e2   ### if we del only one object desc is not work bcoz we have to del both name of object to access destructor





