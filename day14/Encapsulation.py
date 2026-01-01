class Student:
    def __init__(self,name):
        self.sname=name
        self.__marks=0  #private variable

    # getter method
    def get_marks(self):
        return self.__marks

    # setter method
    def set_marks(self,marks):
        if marks<=100:
            self.__marks = marks
        else:
            print("Invalid marks. Marks must be <=100")

stu= Student("student1")
stu.set_marks(99)
print(stu.get_marks())

