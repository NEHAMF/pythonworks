from re import*
text="abc"
pattern="a+"
match=finditer(pattern,text)
for m in match:
    print(m.start())
    print(m.group())

    #[A-Z a-z][A-Z a-z 0-9]*