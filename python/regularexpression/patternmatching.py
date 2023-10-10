from re import *
text="ABABCDefAB234@!&%1"
pattern="AB"
# pattern="[A-Z]"  
# pattern="[a-z,A-Z,0-9]"
# pattern="[^a-z,0-9]"
# pattern="\D"#[^ 0-9]
# pattern="\d" NUMBERS#[0-9]
# pattern="\w" #all words ALPHANUMERIC
# pattern="\W" #SPECIAL CHARACTERS
matcher=finditer(pattern,text)
for m in matcher:
#  print(m.start()) 
    print(f"{m.start()} {m.group()}")    
#  print(m.group())
 
