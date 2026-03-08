class f300:
    general_name ="xyz"
    def __init__(self,name='xyz', roomNumber=0):# can also name self as anything 'myobject'
        self.name=name
        self.roomNumber= roomNumber
    def detailTyper(self):
        print(f"hello my name is {self.name} and i recide in room{self.roomNumber}") 
        self.nextroom = self.roomNumber+1
    


p1=f300("abd",305)
p1.detailTyper()
print(p1.nextroom)
p1.general_name