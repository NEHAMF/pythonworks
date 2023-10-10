lst=[2,3,4,5]
sum=8
low=0
upp=len(lst)-1
while(low<upp):
 curr_sum=lst[low]+lst[upp]
 if curr_sum==sum:   
    print("pairs",lst[low],lst[upp])
    break
 elif curr_sum<sum:
        low=low+1
 else:
        upp=upp-1    
 
