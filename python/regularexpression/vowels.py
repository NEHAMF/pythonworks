from re import *
text="goodmorning #sachin"
# print all vowels using re
pattern="[a e i o u]"
# pattern="[^aeiou\W\d]"
matcher=finditer(pattern,text)
for m in matcher:
    print (m.start(),m.group())
