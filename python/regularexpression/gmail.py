# 
from re import*
gmail_id=input("enter a gmailid")
rule="[a-z,0-9][\W\w]+[@]gmail[.]com"
matcher=fullmatch(rule,gmail_id)
print("invalid" if matcher==None else "valid") 

# valid password
# atleast 1 uppercase
# atleast 1 special characters
# minimum of 8 characters
