class person:
    def __init__(self):
        self.legs = 2

class student(person):
    def __init__(self, age,name):
        super().__init__()
        self.age = age
        self.name = name
        
    def getDetails(self):
        print("details == {} {}".format(self.age, self.name))
        
        
class library(student):
    def __init__(self, age, name):
        super().__init__(age,name)
        student.__init__(self,age,name)  #does same things
        
    
obj1 = library(12,"Tushar")
print("details == {} {}".format(obj1.age, obj1.name))

obj2 = library(12,"Tushar")
print("details == {} {} {}".format(obj1.age, obj1.name, obj2.legs))

