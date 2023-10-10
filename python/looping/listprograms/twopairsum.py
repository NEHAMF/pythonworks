lst=[2,3,4,5,]
sum=6
count=1

# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         cur_sum=lst[i]+lst[j]
#         if cur_sum==sum:
#             print("pairs",lst[i],lst[j])
low=0
upp=len(lst)-1
while(low<upp):
    cur_sum=lst[low]+lst[upp]
    if cur_sum==sum:
     print("pairs",lst[low],lst[upp])
     break
    elif cur_sum<sum:
        low=low+1
    else:
        upp=upp-1   
    count=count+1
    print(count)         


