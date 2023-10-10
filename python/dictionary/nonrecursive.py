text="ABBCCDEF"
chr_count={}
# for ch in text:
#     if ch in chr_count:   #<ippa vannatolla character dic il indonn nokann#
#         chr_count[ch]+=1
#     else:
#         chr_count[ch]=1
# for k,v in chr_count.items():
#     if v==1:
#         print(k)     
for ch in text:
    if ch in chr_count:
        chr_count[ch]+=1
    else:
        chr_count[ch]=1
print(chr_count)     
for k,v in chr_count.items():

    if v==1:
        print(k)
           