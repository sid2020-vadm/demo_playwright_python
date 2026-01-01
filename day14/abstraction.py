
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

# concrete methods implemented from abstract class
class Car(Vehicle):
    def start(self):
        print("engine start")

    def stop(self):
        print("engine stop")


cm1=Vehicle() # cannot possible
v=Car()
v.start()
v.stop()
