from re import*
# pattern="\d{10}"
text="aaabbcaadf"
# pattern="a*" zero or more occurence of a
# pattern="a+" one or mora occurence a
pattern="a{1,2}"
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())