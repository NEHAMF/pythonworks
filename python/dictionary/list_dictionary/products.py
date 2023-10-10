items=[
    {"id":1,"name":"sugar","price":40,"avl_qty":10},
    {"id":2,"name":"milk","price":28,"avl_qty":40},
    {"id":3,"name":"teapowder","price":230,"avl_qty":100},
    {"id":4,"name":"tomatto","price":120,"avl_qty":5},
    {"id":5,"name":"potatto","price":45,"avl_qty":70},
    {"id":6,"name":"carrot","price":80,"avl_qty":0},
    {"id":7,"name":"oreo","price":45,"avl_qty":0},
    {"id":8,"name":"hideandseek","price":50,"avl_qty":50},
    
]
# print total number of products
# print all product names
# print all in stock product names
# print product names avaialble under rs 50
# print all product names avilable in range of 20 to 50


# print(len(items))

# for b in items:
#  print(b.get("name"))

# for b in items:
    # if b.get("avl_qty")>0:
    #  print(b.get("name"))

# for b in items:
    # if b.get("price")<50:
    #   print(b.get("name")):

# for b in items:
#    if b.get("price")in range(20,51):
    #  print(b.get("name"))


# all_name=[i.get("name") for i in items]
# print(all_name)

# in_stock=[i.get("name")  for i in items if i.get("avl_qty")>0]
# print(in_stock)


# price=[i.get("name")  for i in items if i.get("price")<50]
# print(price)

# range=[i.get("name")for i in items if i.get("price")in range(20,51)]
# print(range)

# oreo_price=[i.get("price")for i in items if i.get("name")=="oreo"]
# print(oreo_price)

# oreo_data=[i for i in items if i.get("name")=="oreo"][0]
# oreo_data["price"]=90
# print(oreo_data)
# oreo_price=[i .get("price")for i in items if i.get("name")=="oreo"][0]
# print(oreo_price)

costly_prdt=max(items,key=lambda d:d.get("price"))
print(costly_prdt)
cheapest_Prdct=min(items,key=lambda c:c.get("price"))
print(cheapest_Prdct)







