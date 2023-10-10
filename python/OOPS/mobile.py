class Mobile:
    
    def mob(self):
        print("oneplus")
    def car(self):
        print("polo")
    def bike(self):
        print("ktm")
class Child(Mobile):
    def bike(self):
        print("pulsur")             
object=Child()
object.car()
object.mob()
object.bike()
