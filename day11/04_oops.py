# local ,global and class variables

i,j=10,20 #global variables
class MyClass:
    a,b=30,40 # class variables
    def add(self,x,y): #x,y local variables
       print(x+y) #local variables
       print(self.a+self.b) #class variables
       print(i+j) #global variables

mc1= MyClass()
mc1.add(100,300)


