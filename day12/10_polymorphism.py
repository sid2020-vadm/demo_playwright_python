# overloading
class Human:
    def hello(self,name=None):
        if name is not None:
            print("hello "+name)
        else:
            print("hello")

h= Human()
h.hello()
h.hello("jack")
