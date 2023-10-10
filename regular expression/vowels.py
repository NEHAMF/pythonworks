from re import*
text="good morning #sachin889"
# pattern="[aeiou]"
pattern="[^aeiou\W\d]"
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start())
    print(m.group())