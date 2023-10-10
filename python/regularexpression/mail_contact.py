from re import*
f=open("C:\\Users\\Hamad\\Desktop\\python\\regularexpression\\mail_con.txt")
contact_rule="[\d]{10}"
mail_rule="[\w]+@gmail.com"
mail_id=[]
contact_no=[]
for i in f:
    word=i.rstrip("\n").split(" ")
    # print(word)
    for w in word:
     matcher=fullmatch(mail_rule,w)
     con_matcher=fullmatch(contact_rule,w)
     if matcher!=None:
        mail_id.append(w)
     elif con_matcher!=None:
        contact_no.append(w)
print(mail_id)
print(contact_no)
