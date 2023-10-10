class Student:
    def __init__(self,name,course):
        self.name=name
        self.course=course
    def get_student(self):
        print("my name is ",self.name,"and my course is ",self.course)    
obj=Student("sukumar","python")
obj.get_student()
obj1=Student("Neha","python")
obj1.get_student()
