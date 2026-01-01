class Student():
    def __init__(self, id, name, grad):
        self.sid = id
        self.sname = name
        self.sgrad = grad

    def displaystu(self):
        print(f"stuid {self.sid} stuname {self.sname} stgrad {self.sgrad}")