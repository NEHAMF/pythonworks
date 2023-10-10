text="ABBCDDEF"
non_lst=[]
# wc={}
dup_list=[]
for ch in text:
    if ch in non_lst:
        dup_list.append(ch)
    else:
        non_lst.append(ch) 

print(dup_list[1])   