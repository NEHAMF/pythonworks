class Car:
    def start(self):
        print("key start")
    def break_type(self):
        print("drum break")
    def transmission(self):
        print("manual")
class Ambassador(Car):#Ambassador is a car
    pass    
# obj=Ambassador()
# obj.start()    

class Marutieight(Car):
    def break_type(self):
        print("disc_type")
obj=Marutieight()
obj.break_type()    
        
