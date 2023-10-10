from re import*
vehicle_num=input("enter a vehiclenumber")
rule="(KL)-[\d]{2}-[A-Z]{1,2}-[\d]{4}"
matcher=fullmatch(rule,vehicle_num)
print("invalid" if matcher==None else "vaid") 