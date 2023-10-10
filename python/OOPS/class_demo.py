# class  > building>design=create buliding using plan   >attribute ,methods in class
# object > things that construct using class
# self > used to point current object
# class bottle: 
#  attributes> capacity    instance variables
              # material
              # colour
              # weight
              # cap
# methods> drink()
           #open()
           #fill()
           #close()

# class list:
#   def append()
# def sort()   


class Employee:
    id:int
    name:str
    gender:str
    department:str
    salary:int

    def create(self,id,name,gender,department,salary): #initialising instance variables  
      self.id=id
      self.name=name
      self.department=department
      self.gender=gender
      self.salary=salary
    def get(self):
        print(self.id,self.name,self.gender,self.department,self.salary)


# creating object > class name object
# reference(variable)=classname()


emp1=Employee()
emp1.create(100,"neha","female","hr",32000)
emp1.get()
emp2=Employee()
emp2.create(101,"hafjan","male","hr",35000)
emp2.get() 