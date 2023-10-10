n1=int(input("enter the first number "))#100
n2=int(input("enter the second number "))#20
n3=int(input("enter the third  number "))#15
if(n1>n2)and(n1>n3):
    if(n2>n3):
        print("n1,n2,n3")
    else:
        print("n1,n3,n2")
elif(n2>n1)and(n2>n3):
    if(n1>n3):
      print("n2,n1,n3")
    else:
     print("n2,n3,n1")  
elif(n3>n2)and(n3>n1):
    if(n1>n2):
     print("n3,n1,n2")
    else:
       print("n3,n2,n1")
elif(n1==n2)and(n1==n3):
    print("n1,n2,n3 are equal")  