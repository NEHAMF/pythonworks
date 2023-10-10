exp=[300,9000,6000,7000,80]
# total=0
# for e in exp:
#  total=total+e
# print(total)


#max exp
max_exp=0
for e in exp:
    #e=300
  if e>max_exp:
    max_exp=e
print(max_exp)    


# min_exp=exp[0]
# for e in exp:
#     if e<min_exp:
#         min_exp=e
# print(min_exp)        


# print(min(exp))
# print(max(exp))
# print(sum(exp))
srt_exp=sorted(exp,reverse=True)
print(srt_exp)
