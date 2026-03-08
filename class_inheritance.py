#parent class
# 
class person:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks 
#child class 
class student(person):
    pass

p1=student("abd",26,200) # inherits the properties of person class 
print("name",p1.name)
print("age",p1.age)
print("marks",p1.marks)
        