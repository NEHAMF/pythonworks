class Parent:
  phone="samsunga55" 
  bike="passionpro"
  def mobile(self):
    print(self.phone)
  def vehicle(self):
    print(self.bike)
class Child(Parent):
   pass
obj=Child()
obj.mobile()
obj.vehicle() 