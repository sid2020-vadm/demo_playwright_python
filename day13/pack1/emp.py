class Employee():
    def __init__(self,id,name,grad):
        self.eid=id
        self.ename=name
        self.egrad=grad

    def displayemp(self):
        print(f"etuid {self.eid} etuname {self.ename} etgrad {self.egrad}")
