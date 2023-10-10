from re import*
phone=input("enter a number")
pattern="\d{10}"
matcher=fullmatch(pattern,phone)
if matcher==None:
    print("invalid")
else:
    print("valid")    
