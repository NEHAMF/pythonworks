class Calculator: #same method name different parameters
    def add(self,n1,n2):
        print(n1+n2)
    def add(self,n1,n2,n3):
        print(n1+n2+n3)
obj=Calculator()
obj.add(18,9,8)    
