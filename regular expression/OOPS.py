class Employee:
    id:int
    name:str
    age:int
    gender:str

    def add(self,id,name,gender,age):
        self.id=id
        self.name=name
        self.gender=gender
        self.age=age
    def display(self):
        print(self.id,self.name,self.gender,self.age)    
obj1=Employee()
obj1.add(2,"neha","female",15)
obj1.display()        
