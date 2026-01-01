class MyClass:
    a,b=20,30 # class variables
    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a * self.b)

mc1=MyClass()
mc1.add()
mc1.mul()

