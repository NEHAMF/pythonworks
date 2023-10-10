class Student:
   rollno:int
   name:str
   gender:str
   course:str

   def create(self,rollno,name,gender,course):
       self.rollno=rollno
       self.name=name
       self.gender=gender
       self.course=course
   def display(self):
       print(self.rollno,self.name,self.gender,self.course)
std1=Student()
std1.create(100,"neha","female","python")
std1.display()
std2=Student()
std2.create(101,"aysha","female","big data")
std2.display()       