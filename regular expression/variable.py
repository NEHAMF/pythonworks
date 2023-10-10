from re import*
variable=input("enter a variable")
pattern="[A-Z a-z][\w_]*"
matcher=fullmatch(pattern,variable)
if matcher==None:
    print(" variable is invalid")
else:
    print("valid")    


    #rule k-m
    # second placel digit