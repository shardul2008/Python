'''class Demo:
    def show(self,name,city,mobileno):
        print("name:",name)
        print("City:",city)
        print("Mobileno:",mobileno)
obj = Demo()
obj.show("iGap Technologies","Kolhapur","8767811254") '''

class Demo:
    def __init__(self,name,city,mobileno):
        self.name = name
        self.city = city
        self.mobileno = mobileno   
    
    def show(self):
        print("name:",self.name)
        print("City:",self.city)
        print("Mobileno:",self.mobileno)

obj = Demo("iGap","Kolhapur","5565246486")
obj.show()
