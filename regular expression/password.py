from re import*
password="ssword@123"
rule="(?=.*[A-Z])(?=.*[\d])(?=.*[\W]).{8,}"
matcher=fullmatch(rule,password)
if matcher==None:
    print("invalid")
else:
    print("valid")    