# # source_word="decreases"
# # t_word="dress"
source_word="chicken"
t_word="hen"
source_list=[]
kangaroo_string=""
for k in source_word:
    source_list.append(k)
for k in t_word:
    if k in source_list:
        source_list.remove(k)
        kangaroo_string+=k
print("kangarroo word" if t_word==kangaroo_string else "not kangaroo word")        



# dictionary
# source_word="decreases"
# target_word="dress"
# wc={}
# for ch in source_word:
#     if ch in wc:
#         wc[ch]+=1
#     else:
#         wc[ch]=1
# for ch in target_word:
#     if ch in wc and wc.get(ch)>0:
#         wc[ch]-=1
              
#     else:
#         print("not kangaroo word")
#         break            
