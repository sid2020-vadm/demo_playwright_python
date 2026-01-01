
class A:
    def m1(self):
        print("class A from method m1")

class B(A):
    def m2(self):
        print("class B from method m2")

mc1 = B()
mc1.m1()
mc1.m2()



