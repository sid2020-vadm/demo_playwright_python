# Hierarchy inheritance

class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B(A):
    a, b = 300, 200
    def m2(self):
        print(self.a-self.b)

class C(A):
    e,f = 400,600
    def m3(self):
        print(self.e * self.f)

mc1=B()
mc1.m1()
mc1.m2()

mc2=C()
mc2.m1()
mc2.m3()