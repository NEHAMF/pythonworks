lst=[12,14,16,18,20]
element=16
i=0
stop=len(lst)
# is_found=False   linear searching
while(i<stop):
    current_value=lst[i]
    if current_value==element:
        is_found=True
        break
    i=i+1
print(is_found)    

  