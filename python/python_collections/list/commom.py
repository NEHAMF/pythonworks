# arr=[3,2,4,2]
# arr.sort()
# for i in range(0,len(arr)-1):
#     current=arr[i]
#     next=arr[i+1]
#     if current==next:
#        print(current)

#find least positive missing integer number
arr=[1,3,4,6,5]
arr.sort()
for i in range(0,len(arr)-1):
    current=arr[i]
    next=arr[i+1]
    if next-current!=1:
     print(current+1)
