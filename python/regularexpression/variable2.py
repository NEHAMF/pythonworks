from re import*
variable=input("enter a variable name")
rule="[k-m][369][\w]*"
matcher=fullmatch(rule,variable)
print("in valid" if matcher==None else "valid")