# start=int(input("enter the starting number"))
# range=int(input("please enter the range"))
# sum=0
# while(start<=range):
#     if(start%2!=0):
#          sum=sum+start
#     start=start+1
# print(sum)            


#sum of even numbers

start=int(input("enter the starting number"))
range=int(input("please enter the range"))
sum=0
while(start<=range):
    if(start%2==0):
         sum=sum+start
    start=start+1
print(sum)            