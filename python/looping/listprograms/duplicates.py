# arr=[5,2,5,3,2]
# arr.sort()
# for i in range(0,len(arr)-1):
#     current=arr[i]
#     next=arr[i+1]
#     if current==next:
#         print(current)

arr=[1,3,4,6,5]
#find the least +ve mising number(2) #sort
arr.sort()#[1,3,4,5,6]
for r in range(0,len(arr)-1):
    current=arr[r]
    next=arr[r+1]
    if next-current!=1:
        print(current+1)

