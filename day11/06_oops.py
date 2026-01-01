#class with constructor
# __init__()
# used for initialization
# invoked automatically when object is created

class MyClass:
    def __init__(self):
        print("this is constructor")

    def m1(self):
        print("Hello..")

    def m2(self,x,y):
        return x+y

mc1=MyClass()
mc1.m1()
print(mc1.m2(3,4))
