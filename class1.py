'''class Demo:
    def show(self,name,city,mobileno):
        print("name:",name)
        print("City:",city)
        print("Mobileno:",mobileno)
obj = Demo()
obj.show("iGap Technologies","Kolhapur","8767811254") '''

'''class Demo:
    def __init__(self,name,city,mobileno):
        self.name = name
        self.city = city
        self.mobileno = mobileno   
    
    def show(self):
        print("name:",self.name)
        print("City:",self.city)
        print("Mobileno:",self.mobileno)

#obj = Demo("iGap","Kolhapur","5565246486")
#obj.show()
name = input("Enter name:")
city = input("Enter city:")
mobileno = input("Enter Mobile no.:")
obj = Demo(name,city,mobileno)
obj.show()'''

class Arith:
    def add(a,b):
        print("add:",a+b)
    def sub(a,b):
        print("sub:",a-b)
    def mul(a,b):
        print("mul:",a,b)
    def div(a,b):
        print("div:",a/b)
obj = Arith
obj.add(3,4)
obj.sub(3,5)
obj.mul(5,6)
obj.div(4,8)