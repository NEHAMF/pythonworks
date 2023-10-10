num=371
sum=0
o=num
while(num!=0):
    digit=num%10
    cube=digit**3
    sum=sum+cube
    num=num//10
print(sum)    
print("armstrong" if sum==0 else "not armstrong") 