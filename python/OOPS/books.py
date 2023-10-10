class Books:
    name:int
    author:str
    price:int
    pages:int
    def __init__(self,name,author,price,pages):
        self.name=name
        self.author=author
        self.price=price
        self.pages=pages
    # initialising instance variables
    def get(self):
        print(self.name,self.author,self.price,self.pages)
    def __str__(self):
        return self.author+self.name
obj=Books("aadujeevitham","benyamin",580,615)        
print(obj.name)
obj2=Books("aarachar","meera",560,780)
print(obj.pages)
print(obj)

