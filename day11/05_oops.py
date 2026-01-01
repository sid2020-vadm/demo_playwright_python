a,b=10,20 #global variables
class MyClass:
    a,b=30,40 # class variables
    def add(self,a,b): # local variables
       print(a+b) #local variables
       print(self.a+self.b) #class variables
       print(globals()['a']+globals()['b']) #global variables

mc1= MyClass()
mc1.add(100,300)