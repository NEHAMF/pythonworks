from re import*
variable=input("enter a variable name ")
rule="[A-Za-z][\w_]*"
matcher=fullmatch(rule,variable)
print("invalid" if matcher==None else "valid")
# rule first k-m   second must be a digit divisible by 3 any num