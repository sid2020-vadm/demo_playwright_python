class Calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)

cal = Calculation()
cal.add()
cal.add(10)
cal.add(10,20)
cal.add(10,20,30)
