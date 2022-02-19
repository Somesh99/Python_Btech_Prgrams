class employee:
    def __init__(self):  ### constructor
        self.name='somesh' ### public
        self.__age=19     ###  private
    def disp(self):
        print(self.name,self.__age)
e1=employee()     ### object creation
e1.disp()         ### calling member function
print(e1.name)
##print(e1.__age)   ### private member not exist outside the class
print(e1._employee__age) ### to access the private member outside the class, add _classname before __age

