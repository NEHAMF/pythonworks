year=int(input("enter a year"))
if(year%100==0)and(year%400==0):
    print("it is leap year",year)
elif(year%100!=0)and(year%4==0):
    print("it is leap year",year)
else:
    print("it is not leap year")        