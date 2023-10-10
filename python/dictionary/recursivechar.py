text="BACDEB"
WC={}
for ch in text:
    if ch in WC:
        print(ch,"is the first recursive character")
        break
    else:
        WC[ch]=1
# print(WC)            

