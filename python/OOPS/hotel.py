class Hotel:
    items=[
        {"id":10,"name":"cb","price":160},
        {"id":101,"name":"vb","price":140},
        {"id":102,"name":"ghhe roast","price":120},
        {"id":103,"name":"afm","price":130},
        {"id":104,"name":"cf","price":90},
        {"id":105,"name":"porotta","price":10},
    ]
    def create(self,*args,**kwargs):
        self.items.append(kwargs)
        return f"{kwargs} created"
# obj=Hotel()
# print(obj.create(id=106,name="noodles",price=180))   
    def retreive(self,id=None,*args,**kwargs):
        obj=[i for i in self.items if i.get("id")==id][0]
        return obj
# obj=Hotel()
# print(obj.retreive(id=101))
    def destroy(self,id=None,*args,**kwargs):
        obj=[i for i in self.items if i.get("id")==id][0]
        self.items.remove(obj)
        return f"{obj}has been removed"
# obj=Hotel()
# print(obj.destroy(id=102)

    def update(self,id=None,*args,**kwargs):
        obj=self.retreive(id=id)
        obj.update(kwargs)
        return f"{kwargs} has been updated"
obj=Hotel()
print(obj.update(id=102,name="Ghee roast"))

# == value same
# is-