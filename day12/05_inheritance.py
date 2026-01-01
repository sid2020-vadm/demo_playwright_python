# multiple inheritance
class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B:
    a, b = 300, 200
    def m2(self):
        print(self.a-self.b)

class C(A,B):
    e,f = 400,600
    def m3(self):
        print(self.e * self.f)

mc1=C()
mc1.m1()
mc1.m2()
mc1.m3()