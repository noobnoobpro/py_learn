if 0:
    class vehicle:
        def __init__(self,name,age):
            self.name=name
            self.__age=age #private property age
        def display_age(self):
            print(f"the age is {self.__age}")

    object1=vehicle("corolla",2020)
    print(object1.__age)
    #object1.display_age()
        

# now lets write a class function that uses encapsulation to hide an age and modify an age

class admin_access:
    def __init__(self,name,password):
        self.name=name
        self.__password=password 
    def admin(self,__name):
        if __name =="abd":
            try:
                pass
            except:
                print(f"Error 404: Cannot modify admin {__name} password ")
        return __name
    def users(self,name, password):
        self.name=name
        self.__password= password

a1=admin_access("abd","xyz")
print(a1.admin("Name"))
