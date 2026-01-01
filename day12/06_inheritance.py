#method overriding

class A:
    def m1(self):
        print("this is m1 from A class")

class B(A):
    def m1(self):
        print("this is m1 from class B")
        super().m1() #invoke the immediate parent class method

mc1= B()
mc1.m1()
