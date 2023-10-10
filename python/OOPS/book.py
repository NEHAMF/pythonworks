class Book:
    def __init__(self) -> None:
        self.id=int(input("enter the id "))
        self.title=input("enter the name ")
        self.author=input("enter the author ")
        self.price=int(input("enter the price "))
    def getauthor(self):
        print(self.author)    
    def gettitle(self):
        print(self.title)
    def setprice(self):
        self.price=int(input("enter the price "))
    def ge_ttitle(self):
        self.title=input("enter the name ") 
b1=Book()
b1.getauthor()
b1.gettitle()
