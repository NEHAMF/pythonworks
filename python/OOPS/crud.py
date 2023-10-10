items=[
    {"id":10,"name":"cb","price":160},
    {"id":101,"name":"vb","price":140},
    {"id":102,"name":"ghhe roast","price":120},
    {"id":103,"name":"afm","price":130},
    {"id":104,"name":"cf","price":90},
    {"id":105,"name":"porotta","price":10},

]
# def add_item(*args,**kwargs):
#     items.append(kwargs)
# add_item(id=106,name="neha",price=180)
# print(items)    

def retreive_item(id=None,*args,**kwargs):
   obj=[i for i in items if i.get("id")==id]
   return obj
# print(retreive_item(id=102))

def destroy_item(id=None,*args,**kwargs):
   obj=[i for i in items if i.get("id")==id][0]
   items.remove(obj)
destroy_item(id=101)   
# print(items)

def update_item(id=None,*args,**kwargs):
   obj=[i for i in items if i.get("id")==id]
   obj.update(kwargs)
update_item(id=101,name="GHEE ROAST")   
print(retreive_item(id=101))
# mobiles id name brand price