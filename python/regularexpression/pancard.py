from re import*
pancard_num=input("enter pancard number")
rule="[A-Z]{3}[PCFTHA]{1}[A-Z]{1}[\d]{4}[A-Z]{1}"
matcher=fullmatch(rule,pancard_num)
print("invalid"if matcher==None else "valid")