#calling parent class variables using child class
class A:
    a,b=10,20

class B(A):
    c,d=100,200
    def m1(self,x,y):
        print(x+y) #local variable
        print(self.c+self.d) #B class variables
        print(self.a+self.b) #A class variables

mc1=B()
mc1.m1(1000,2000)