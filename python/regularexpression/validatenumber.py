from re import*
phone=input("enter a number")
rule="\d{10}"
matcher=fullmatch(rule,phone)
if matcher==None:
    print("INVALID")
else:
    print("VALID")    
