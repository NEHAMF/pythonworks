num=324
sum=0
#3+2+4 =9
while(num!=0):
  digit=num%10
  sum=sum+digit
  num=num//10
print(sum)