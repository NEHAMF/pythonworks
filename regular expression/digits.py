from re import*
text="i have 2 car 2 bikes 3 cycles"
pattern="[0-9]+"
matcher=finditer(pattern,text)
for m in matcher:
    print(m.group())
