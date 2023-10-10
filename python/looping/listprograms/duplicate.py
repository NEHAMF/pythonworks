text="malayalam"
count=len(text)-1
p=""
for i in range(count,-1,-1):
    p=p+text[i]
print("paliandrome" if text==p else "not paliandrome")    



