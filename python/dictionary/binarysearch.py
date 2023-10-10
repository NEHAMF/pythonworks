#    data structure and algorithm >linear search will be in sorted array
# binary search
# word count
# first recursive
#   sort
#  bubble sort
# merge sort
# dfs
# bfs
# dijkstra algorithm


# binary search
# worst case
# edge case

lst=[12,3,4,10,16,18]
lst.sort()
element=18
is_found=False
low=0
upp=len(lst)-1
while(low<=upp):
     mid=(low+upp)//2     

     if element==lst[mid]:
      is_found=True
      break
     elif element<lst[mid]:
        upp=mid-1
     elif element>lst[mid]:
        low=mid+1
print(is_found)          
   




