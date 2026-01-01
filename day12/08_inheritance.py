# overriding variables

class A:
    name="john"
class B(A):
    name="amit" #overriding class A variable
    def m1(self):
        print(super().name) #access parent class variable
mc1=B()
print(mc1.name)
mc1.m1()
