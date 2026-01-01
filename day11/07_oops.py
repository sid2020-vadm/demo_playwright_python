# constructor with parameters and class variables
# class MyClass:
#     name = "John" # class variable
#
#     def __init__(self,id):
#         print(id)
#         print(self.name)
#
# m1=MyClass(123)

# creating class variables inside constructors
class Emp:
    def __init__(self,id,name,sallary):
        self.eid = id
        self.ename =name
        self.esallary=sallary
    def display(self):
        print(self.eid,self.ename,self.esallary)

mc1= Emp(101,"john",1234)
mc1.display()

mc3= Emp(202,"jack",5678)
mc3.display()
