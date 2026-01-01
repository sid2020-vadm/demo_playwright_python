class Employee():
    def m1(self):
        print("this is instance method")
    @staticmethod
    def m2(num):
        print(num)

mc1=Employee()
mc1.m1()
mc1.m2("vishrut")

Employee.m2("john")
