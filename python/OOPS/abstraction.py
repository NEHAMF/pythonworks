# hide implenmentation details
from abc import ABC,abstractmethod
class Bike(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def breaks(self):
        pass
    @abstractmethod
    def accelerate(self):
        pass  
class Hunter(Bike):
    def start(self):
        print("hunter starts")
    def breaks(self):
        print("hunter stops")
    def accelerate(self):
        print("hunter accelerate")
obj=Hunter()
obj.start()
obj.accelerate()
obj.breaks()                  