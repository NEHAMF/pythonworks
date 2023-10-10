orders=["vegmeals","fismeals","vegmeals","bb","fishmeals","bb","cc","vb","bb","vegmeals","fishmeals","fried rice"]
# if key in dic_o_bj
# order_count={}
# for item in orders:
#     if item in order_count:
#         order_count[item]+=1
#     else:
#        order_count[item]=1    
# print(order_count)     
order_count={}
for item in orders:
    if item in order_count:
        order_count[item]+=1
    else:
        order_count[item]=1
print(order_count)            

