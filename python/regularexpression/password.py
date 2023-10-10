from re import*
# password=input("enter a password")
# rule="[A-Z\w]{8}"
# matcher=fullmatch(password,rule)
# print("invalid" if matcher==None else "valid")
password="password@123"
rule="(?=.*[A-Z])(?=.*[\W])(?=.*[\d]).{8,})"
matcher=fullmatch(rule,password)
print("valid" if matcher!=None else "invalid")
 
