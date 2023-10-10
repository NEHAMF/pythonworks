class P1:
    def m1(self):
        print("inside class P1 m1 is a method")
class P2:
    def m2(self):
        print("inside class P2 m2 is a method")
class child(P2,P1):
    def m3(self):
         print("inside class P2 m3 is a method")  

obj=child()
obj.m1()  
obj.m2()
obj.m3()
        