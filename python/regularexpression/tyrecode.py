from re import*
# f=open("C:\\Users\\Hamad\\Desktop\\fullstack\\python\\regularexpression\\tyre.txt","w")
tyre_code=input("enter tyre code")
rule="[\d]{3}[/][\d]{2}[R][\d]{2}[/][\d]{2}[A-Z]"
matcher=fullmatch(rule,tyre_code)
print("invalid"if matcher==None else "valid")